"""
This script takes a GEO soft file, parses it, and then retrieves the listed file via FTP.
"""
import io
from ftplib import FTP
from urlparse import urlparse
from os.path import basename
from os.path import join
from os.path import normpath
import sys
#import argparse

#def get_value(line):
#search_headers = ["^SERIES", "^SAMPLE", "!Sample_supplementary_file"]

parse_file = 'GSE36104_family.soft'
filetype_search = ['.txt', '.bed' ]
ftp_server = 'ftp.ncbi.nlm.nih.gov'
ftp_user = 'anonymous'
ftp_password = 'kandril@bu.edu'

def value_has_filetype(value):
    for filetype in filetype_search:
        if filetype in value:
            return True
    return False

def download_files(results_dict, dir_out):
    ftp = FTP(ftp_server)
    ftp.login(ftp_user, ftp_password)
    for key in results_dict:
        url = urlparse(results_dict[key])
        
        file = open(join(dir_out, basename(url.path)), 'wb', 'utf-8')
        print 'Downloading: ' + basename(url.path)
        ftp.retrbinary('RETR ' + url.path, file.write)
        file.close()

def main():
    parse_file = sys.argv[1]
    dir_out = normpath(sys.argv[2])
    results = dict()
    #TODO find alternative to io.open that does not require the terminal to use en_US.utf8 locale
    for line in io.open(parse_file):
        key, value = line.strip().split(' = ')
        if key == '^SERIES':
            series_id = value
        elif key == '^SAMPLE':
            sample_id = value
        elif key.startswith('!Sample_supplementary_file') and value_has_filetype(value):
            results[sample_id] = value

    output = open(series_id + '_log.txt', 'w')
    output.write("Sample ID" + '\t' + "File URI")
    output.write('\n')
    for key in results:
        output.write(key + '\t' + results[key])
        output.write('\n')
    output.close()

    download_files(results, dir_out)

if __name__ == "__main__":
    main()





