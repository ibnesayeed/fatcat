
Run in order:

- ISSN
- ORCID
- Crossref
- Manifest

Lots of trouble with encoding; always `export LC_ALL=C.UTF-8`

## Data Sources

Download the following; uncompress the sqlite file, but **do not** uncompress
the others:

    https://archive.org/download/crossref_doi_dump_201801/crossref-works.2018-01-21.json.xz
    https://archive.org/download/ia_papers_manifest_2018-01-25/index/idents_files_urls.sqlite.gz
    https://archive.org/download/ia_journal_metadata_explore_2018-04-05/journal_extra_metadata.csv
    https://archive.org/download/issn_issnl_mappings/20180216.ISSN-to-ISSN-L.txt
    https://archive.org/download/orcid-dump-2017/public_profiles_API-2.0_2017_10_json.tar.gz

## ISSN

From CSV file:

    time ./client.py import-issn /srv/datasets/journal_extra_metadata.csv

## ORCID

Directly from compressed tarball:

    tar xf /srv/datasets/public_profiles_API-2.0_2017_10_json.tar.gz -O | jq -c . | grep '"person":' | time parallel -j12 --pipe --round-robin ./client.py import-orcid -

Or, from pre-uncompressed tarball:

    tar xf /srv/datasets/public_profiles_API-2.0_2017_10_json.tar.gz -O | jq -c . | rg '"person":' > /srv/datasets/public_profiles_1_2_json.all.json
    time parallel --bar --pipepart -j8 -a /srv/datasets/public_profiles_1_2_json.all.json ./client.py import-orcid -

Does not work:

    ./client.py import-orcid /data/orcid/partial/public_profiles_API-2.0_2017_10_json/3/0000-0001-5115-8623.json

Instead:

    cat /data/orcid/partial/public_profiles_API-2.0_2017_10_json/3/0000-0001-5115-8623.json | jq -c . | ./client.py import-orcid -

Or for many files:

    find /data/orcid/partial/public_profiles_API-2.0_2017_10_json/3 -iname '*.json' | parallel --bar jq -c . {} | rg '"person":' | ./client.py import-orcid -

### ORCID Performance

for ~9k files:

    (python-B2RYrks8) bnewbold@orithena$ time parallel --pipepart -j4 -a /data/orcid/partial/public_profiles_API-2.0_2017_10_json/all.json ./client.py import-orcid -
    real    0m15.294s
    user    0m28.112s
    sys     0m2.408s

    => 636/second

    (python-B2RYrks8) bnewbold@orithena$ time ./client.py import-orcid /data/orcid/partial/public_profiles_API-2.0_2017_10_json/all.json
    real    0m47.268s
    user    0m2.616s
    sys     0m0.104s

    => 203/second

## Crossref

From compressed:

    xzcat /srv/datasets/crossref-works.2018-01-21.json.xz | time parallel -j12 --round-robin --pipe ./client.py import-crossref - /srv/datasets/20180216.ISSN-to-ISSN-L.txt

## Manifest 

    time ./client.py import-manifest /srv/datasets/idents_files_urls.sqlite