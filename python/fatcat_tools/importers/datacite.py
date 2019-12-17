"""
Prototype Importer for datacite.org data.

Example doc at: https://gist.github.com/miku/5610a2d64e3fee82d16f5d3f3a295fc8
"""

from .common import EntityImporter
import dateparser
import langcodes
import datetime
import langdetect
import fatcat_openapi_client
import json
import sys
import hashlib

# https://guide.fatcat.wiki/entity_container.html#container_type-vocabulary
CONTAINER_TYPE_MAP = {
    'Journal': 'journal',
    'Series': 'journal',
    'Book Series': 'book-series',
}

# The docs/guide should be the cannonical home for these mappings; update there
# first.  Map various datacite type types to CSL-ish types. None means TODO or
# remove.
DATACITE_TYPE_MAP = {
    'ris': {
        'THES': 'thesis',
        'SOUND': None,
        'CHAP': 'chapter',
        'FIGURE': None,
        'RPRT': 'report',
        'JOUR': 'article-journal',
        'MPCT': None,
        'GEN': None,
        'BOOK': 'book',
        'DATA': 'dataset',
        'COMP': None,
    },
    'schemaOrg': {
        'Dataset': 'dataset',
        'Book': 'book',
        'ScholarlyArticle': 'article',
        'ImageObject': 'graphic',
        'Collection': None,
        'MediaObject': None,
        'Event': None,
        'SoftwareSourceCode': None,
        'Chapter': 'chapter',
        'CreativeWork': None,
        'PublicationIssue': 'article',
        'AudioObject': None,
        'Thesis': 'thesis',
    },
    'citeproc': {
        'dataset': 'dataset',
        'chapter': 'chapter',
        'article-journal': 'article-journal',
        'song': 'song',
        'article': 'article',
        'report': 'report',
        'graphic': 'graphic',
        'thesis': 'thesis',
        'book': 'book',
    },
    'bibtex': {
        'phdthesis': 'thesis',
        'inbook': 'chapter',
        'misc': None,
        'article': 'article-journal',
        'book': 'book',
    },
    'resourceTypeGeneral': {
        'Image': None,
        'Dataset': 'dataset',
        'PhysicalObject': None,
        'Collection': None,
        'Text': None,
        'Sound': None,
        'InteractiveResource': None,
        'Event': None,
        'Software': None,
        'Other': None,
        'Workflow': None,
        'Audiovisual': None,
    }
}


# TODO(martin): merge this with other maps, maybe.
LICENSE_SLUG_MAP = {
    "//creativecommons.org/licenses/by/2.0/": "CC-BY",
    "//creativecommons.org/licenses/by/2.0/uk/legalcode": "CC-BY",
    "//creativecommons.org/licenses/by/3.0/": "CC-BY",
    "//creativecommons.org/licenses/by/3.0/us": "CC-BY",
    "//creativecommons.org/licenses/by/4.0/": "CC-BY",
    "//creativecommons.org/licenses/by/4.0/deed.de/": "CC-BY",
    "//creativecommons.org/licenses/by/4.0/deed.en_US/": "CC-BY",
    "//creativecommons.org/licenses/by/4.0/legalcode/": "CC-BY",
    "//creativecommons.org/licenses/by-nc/2.0/": "CC-BY-NC",
    "//creativecommons.org/licenses/by-nc/3.0/": "CC-BY-NC",
    "//creativecommons.org/licenses/by-nc/4.0/": "CC-BY-NC",
    "//creativecommons.org/licenses/by-nc/4.0/legalcode": "CC-BY-NC",
    "//creativecommons.org/licenses/by-nc-nd/3.0/": "CC-BY-NC-ND",
    "//creativecommons.org/licenses/by-nc-nd/3.0/gr": "CC-BY-NC-ND",
    "//creativecommons.org/licenses/by-nc-nd/4.0/": "CC-BY-ND",
    "//creativecommons.org/licenses/by-nc-nd/4.0/legalcode": "CC-BY-ND",
    "//creativecommons.org/licenses/by-nc-sa/4.0/": "CC-BY-NC-SA",
    "//creativecommons.org/licenses/by-nd/4.0/": "CC-BY-ND",
    "//creativecommons.org/licenses/by-sa/3.0/de": "CC-BY-SA",
    "//creativecommons.org/licenses/by-sa/3.0/gr": "CC-BY-SA",
    "//creativecommons.org/licenses/by-sa/4.0/": "CC-BY-SA",
    "//creativecommons.org/licenses/by-sa/4.0/legalcode": "CC-BY-SA",
    "//creativecommons.org/licenses/CC-BY/4.0/": "CC-BY",
    "//creativecommons.org/licenses/publicdomain/zero/1.0/": "CC-0",
    "//creativecommons.org/publicdomain/zero/1.0/": "CC-0",
    "//creativecommons.org/publicdomain/zero/1.0/legalcode": "CC-0",
    "//opensource.org/licenses/MIT": "MIT",
    "//www.elsevier.com/open-access/userlicense/1.0": "ELSEVIER-USER-1.0",
    "//www.gnu.org/licenses/gpl-3.0.en.html": "GPLv3",
    "//www.gnu.org/licenses/old-licenses/gpl-2.0.en.html": "GPLv2",
    "//www.karger.com/Services/SiteLicenses": "KARGER",
    "//www.opensource.org/licenses/Apache-2.0": "Apache-2.0",
    "//www.opensource.org/licenses/BSD-3-Clause": "BSD-3-Clause",
    "//www.opensource.org/licenses/EUPL-1.1": "EUPL-1.1", # redirects to EUPL-1.2
    "//www.opensource.org/licenses/MIT": "MIT",
    # "http://royalsocietypublishing.org/licence": "", # OA and "normal", https://royalsociety.org/journals/authors/licence-to-publish/
    # "http://rsc.li/journals-terms-of-use": "RSC",
    # "http://www.fu-berlin.de/sites/refubium/rechtliches/Nutzungsbedingungen": "", # 53 UrhG.
    # "http://www.nrcresearchpress.com/page/about/CorporateTextAndDataMining": "",
    # "http://www.springer.com/tdm": "",
    # "https://cds.unistra.fr/vizier-org/licences_vizier.html": "", # Maybe try to "SPN" those: https://web.archive.org/web/*/https://cds.unistra.fr/vizier-org/licences_vizier.html
    # "https://link.aps.org/licenses/aps-default-accepted-manuscript-license": "",
    # "https://oparu.uni-ulm.de/xmlui/license_opod_v1": "",
    # "https://publikationen.bibliothek.kit.edu/kitopen-lizenz": "",
    # "https://rightsstatements.org/page/InC/1.0?language=en": "",
    # "https://services.ceda.ac.uk/cedasite/register/info": "",
    # "https://wdc.dlr.de/ndmc/userfiles/file/NDMC-Data_Sharing_Principles.pdf": "", # 404
    # "https://www.cambridge.org/core/terms": "",
    # "https://www.elsevier.com/tdm/userlicense/1.0",
    # "info:eu-repo/semantics/closedAccess": "", # https://wiki.surfnet.nl/display/standards/info-eu-repo/#info-eu-repo-AccessRights
    # "info:eu-repo/semantics/embargoedAccess": "",
    # "info:eu-repo/semantics/openAccess": "",
    # Note: Some URLs pointing to licensing terms are not in WB yet (but would be nice).
}

class DataciteImporter(EntityImporter):
    """
    Importer for datacite records. TODO(martin): Do we need issn_map_file?
    """

    def __init__(self, api, issn_map_file, **kwargs):

        eg_desc = kwargs.get('editgroup_description',
            "Automated import of Datacite DOI metadata, harvested from REST API")
        eg_extra = kwargs.get('editgroup_extra', dict())
        eg_extra['agent'] = eg_extra.get('agent', 'fatcat_tools.DataciteImporter')
        super().__init__(api,
            issn_map_file=issn_map_file,
            editgroup_description=eg_desc,
            editgroup_extra=eg_extra,
            **kwargs)

        self.create_containers = kwargs.get('create_containers', True)
        self.read_issn_map_file(issn_map_file)

    def parse_record(self, obj):
        """
        Mapping datacite JSON to ReleaseEntity.
        """
        if 'attributes' not in obj:
            return None

        attributes = obj['attributes']

        # Contributors. Many nameIdentifierSchemes, we do not use yet:
        # "attributes.creators[].nameIdentifiers[].nameIdentifierScheme": [
        # "LCNA", "GND", "email", "NAF", "OSF", "RRID", "ORCID", "SCOPUS",
        # "NRCPID", "schema.org", "GRID", "MGDS", "VIAF", "JACoW-ID" ],
        contribs = []

        for i, c in enumerate(attributes['creators']):
            if not c.get('nameType') == 'Personal':
                continue
            creator_id = None
            for nid in c.get('nameIdentifiers', []):
                if not nid.get('nameIdentifierScheme').lower() == "orcid":
                    continue
                orcid = nid.get('nameIdentifier', '').replace('https://orcid.org/', '')
                if not orcid:
                    continue
                creator_id = self.lookup_orcid(orcid)
                # If creator_id is None, should we create creators?
            contribs.append(fatcat_openapi_client.ReleaseContrib(
                creator_id=creator_id,
                index=i,
                raw_name=c.get('name'),
                given_name=c.get('givenName'),
                surname=c.get('familyName'),
            ))

        # Title, may come with "attributes.titles[].titleType", like
        # "AlternativeTitle", "Other", "Subtitle", "TranslatedTitle"
        title, subtitle = None, None

        for entry in attributes.get('titles', []):
            if not title and 'titleType' not in entry:
                title = entry.get('title').strip()
            if entry.get('titleType') == 'Subtitle':
                subtitle = entry.get('title').strip()

        # Dates. A few internal dates (registered, created, updated) and
        # published (0..2554). We try to work with typed date list, in
        # "attributes.dates[].dateType", values: "Accepted", "Available"
        # "Collected", "Copyrighted", "Created", "Issued", "Submitted",
        # "Updated", "Valid".
        release_year, release_date = None, None

        date_type_prio = (
            'Valid',
            'Issued',
            'Available',
            'Accepted',
            'Submitted',
            'Copyrighted',
            'Collected',
            'Created',
            'Updated',
        )
        for prio in date_type_prio:
            dates = attributes.get('dates', []) or [] # Never be None.
            for item in dates:
                if not item.get('dateType') == prio:
                    continue
                try:
                    result = dateparser.parse(item.get('date'))
                except TypeError as err:
                    print("{} failed with: {}".format(item.get('date'), err), file=sys.stderr)
                    continue
                if result is None:
                    # Unparsable date.
                    continue
                release_date = result
                release_year = result.year
                if 1000 < release_year < datetime.date.today().year + 5:
                    # Skip possibly bogus dates.
                    continue
                break
            else:
                continue
            break

        # Publisher. A few NA values. A few bogus values.
        publisher = attributes.get('publisher')

        if publisher in ('(:unav)', 'Unknown', 'n.a.', '[s.n.]', '(:unap)', '(:none)'):
            publisher = None
        if publisher is not None and len(publisher) > 80:
            # Arbitrary magic value max length. TODO(martin): better heuristic,
            # but factored out; first we have to log misses. Example:
            # "ETH-Bibliothek Zürich, Bildarchiv / Fotograf: Feller,
            # Elisabeth, Empfänger, Unbekannt, Fotograf / Fel_041033-RE /
            # Unbekannt, Nutzungsrechte müssen durch den Nutzer abgeklärt
            # werden"
            publisher = None

        # Container. For the moment, only ISSN as container.
        container_id = None

        container = attributes.get('container', {}) or {}
        if container.get('type') in CONTAINER_TYPE_MAP.keys():
            container_type = CONTAINER_TYPE_MAP.get(container['type'])
            if container.get('identifier') and container.get('identifierType') == 'ISSN':
                issn = container.get('identifier')
                if len(issn) == 8:
                    issn = issn[:4] + "-" + issn[4:]
                issnl = self.issn2issnl(issn)
                if issnl is not None:
                    container_id = self.lookup_issnl(issnl)

                    if container_id is None and container.get('title'):
                        ce = fatcat_openapi_client.ContainerEntity(
                            issnl=issnl,
                            container_type=container_type,
                            name=container.get('title'),
                        )
                        ce_edit = self.create_container(ce)
                        container_id = ce_edit.ident
                        self._issnl_id_map[issnl] = container_id

        # Volume and issue.
        volume = container.get('volume')
        issue = container.get('issue')

        # Pages.
        pages = None

        first_page = container.get('firstPage')
        last_page = container.get('lastPage')

        if first_page and last_page:
            try:
                int(first_page) < int(last_page)
                pages = '{}-{}'.format(first_page, last_page)
            except ValueError as err:
                print(err, file=sys.stderr)
                pass

        if not pages and first_page:
            pages = first_page

        # License.
        license_slug = None
        license_extra = []

        for l in attributes.get('rightsList', []):
            slug = lookup_license_slug(l.get('rightsUri'))
            if slug:
                license_slug = slug
            license_extra.append(l)

        # Release type. Try to determine the release type from a variety of
        # types supplied in datacite. The "attributes.types.resourceType"
        # contains too many (176 in sample) things for now; citeproc may be the
        # closest, but not always supplied.
        for typeType in ('citeproc', 'resourceTypeGeneral', 'schemaOrg', 'bibtex', 'ris'):
            value = attributes.get('types', {}).get(typeType)
            release_type = DATACITE_TYPE_MAP.get(value)
            if release_type is not None:
                break

        if release_type is None:
            print("datacite unmapped type: {}".format(release_type), file=sys.stderr)

        # Language values are varied ("ger", "es", "English", "ENG", "en-us",
        # "other", ...). Try to crush it with langcodes: "It may sound to you
        # like langcodes solves a pretty boring problem. At one level, that's
        # right. Sometimes you have a boring problem, and it's great when a
        # library solves it for you." -- TODO(martin): We need more of these.
        language = None

        value = attributes.get('language', '') or ''
        try:
            language = langcodes.find(value).language
        except LookupError:
            try:
                language = langcodes.get(value).language
            except langcodes.tag_parser.LanguageTagError:
                print('could not determine language: {}'.format(value), file=sys.stderr)

        # Abstracts appear in "attributes.descriptions[].descriptionType", some
        # of the observed values: "Methods", "TechnicalInfo",
        # "SeriesInformation", "Other", "TableOfContents", "Abstract". The
        # "Other" fields might contain references or related articles (with
        # DOI). TODO(martin): maybe try to parse out some of those refs.
        abstracts = []

        for desc in attributes.get('descriptions', []):
            if not desc.get('descriptionType') == 'Abstract':
                continue
            if len(desc.get('description', '')) < 10:
                continue
            text = desc.get('description')
            sha1 = hashlib.sha1(text.encode('utf-8')).hexdigest()
            lang = None
            try:
                lang = langdetect.detect(text)
            except langdetect.lang_detect_exception.LangDetectException:
                pass
            abstracts.append(fatcat_openapi_client.ReleaseAbstract(
                mimetype="text/plain",
                content=text,
                sha1=sha1,
                lang=lang,
            ))

        # References and relations. Datacite include many relation types in
        # "attributes.relatedIdentifiers[].relationType", e.g.
        # "IsPartOf", "IsPreviousVersionOf", "Continues", "IsVariantFormOf",
        # "IsSupplementTo", "Cites", "IsSupplementedBy", "IsDocumentedBy", "HasVersion",
        # "IsCitedBy", "IsMetadataFor", "IsNewVersionOf", "IsIdenticalTo", "HasPart",
        # "References", "Reviews", "HasMetadata", "IsContinuedBy", "IsVersionOf",
        # "IsDerivedFrom", "IsSourceOf".
        #
        # For the moment, we only care about References.
        refs, ref_index = [], 0

        for rel in attributes.get('relatedIdentifiers', []):
            if not rel.get('relationType') == 'References':
                continue
            ref_extra = dict()
            if rel.get('relatedIdentifierType') == 'DOI':
                ref_extra['doi'] = rel.get('relatedIdentifier')
            if not ref_extra:
                ref_extra = None
            refs.append(fatcat_openapi_client.ReleaseRef(
                index=ref_index,
                extra=ref_extra,
            ))
            ref_index += 1

        # Start with clear stages, e.g. published. TODO(martin): we could
        # probably infer a bit more from the relations, e.g.
        # "IsPreviousVersionOf" or "IsNewVersionOf".
        release_stage = None
        if attributes.get('state') == 'findable' or attributes.get('isActive') is True:
            release_stage = 'published'

        # Extra information.
        extra_datacite = dict()

        if license_extra:
            extra_datacite['license'] = license_extra
        if attributes.get('subjects'):
            extra_datacite['subjects'] = attributes['subjects']
        if attributes.get('url'):
            extra_datacite['url'] = attributes['url']

        extra = dict()

        if extra_datacite:
            extra['datacite'] = extra_datacite

        # Assemble release.
        re = fatcat_openapi_client.ReleaseEntity(
            work_id=None,
            container_id=container_id,
            release_type=release_type,
            release_stage=release_stage,
            title=title,
            subtitle=subtitle,
            original_title=title,
            release_year=release_year,
            release_date=release_date,
            publisher=publisher,
            ext_ids=fatcat_openapi_client.ReleaseExtIds(
                doi=attributes.get('doi'),
            ),
            contribs=contribs,
            volume=volume,
            issue=issue,
            pages=pages,
            language=language,
            abstracts=abstracts,
            refs=refs,
            extra=extra,
            license_slug=license_slug,
        )
        return re

    def try_update(self, re, debug=True):
        """
        When debug is true, write the RE to stdout.
        """
        if debug is True:
            print(json.dumps(re.to_dict(), default=extended_json_encoder))
            return False

        # lookup existing DOI (don't need to try other ext idents for crossref)
        existing = None
        try:
            existing = self.api.lookup_release(doi=re.ext_ids.doi)
        except fatcat_openapi_client.rest.ApiException as err:
            if err.status != 404:
                raise err
            # doesn't exist, need to update
            return True

        # eventually we'll want to support "updates", but for now just skip if
        # entity already exists
        if existing:
            self.counts['exists'] += 1
            return False

        return True

    def insert_batch(self, batch):
        self.api.create_release_auto_batch(fatcat_openapi_client.ReleaseAutoBatch(
            editgroup=fatcat_openapi_client.Editgroup(
                description=self.editgroup_description,
                extra=self.editgroup_extra),
            entity_list=batch))

def extended_json_encoder(value):
    """
    Can be used with json.dumps(value, default=extended_json_encoder) to serialize
    value not serializable by default. https://docs.python.org/3/library/json.html#basic-usage
    """
    if isinstance(value, (datetime.datetime, datetime.date)):
        return value.isoformat()
    if isinstance(value, set):
        return list(value)

def lookup_license_slug(raw):
    """
    TODO(martin): reuse from or combine with crossref, maybe.
    """
    if not raw:
        return None
    raw = raw.strip().replace('http://', '//').replace('https://', '//')
    if 'creativecommons.org' in raw.lower():
        raw = raw.lower()
        raw = raw.replace('/legalcode', '/').replace('/uk', '')
        if not raw.endswith('/'):
            raw = raw + '/'
    return LICENSE_SLUG_MAP.get(raw)
