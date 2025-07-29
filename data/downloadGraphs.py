import boto
import sys
import zipfile
import pandas as pd
from io import BytesIO

if len(sys.argv) != 2:
    print("Usage: python downloadGraphs.py data.csv")
    exit(1)

conn = boto.connect_s3(anon=True)
b = conn.get_bucket("mqlibinstances", validate=False)

for row in pd.read_csv(sys.argv[1])["fname"]:
    k = boto.s3.key.Key(b)
    print(row)
    k.key = row

    fp = BytesIO(k.get_contents_as_string())
    with zipfile.ZipFile(fp, "r") as zfp:
        for filename in zfp.namelist():
            print(filename)
            with open("instances/" + filename, "wb") as f:
                f.write(zfp.read(filename))
        zfp.printdir()

    # if sys.version_info > (3, 0):
    #     sys.stdout.buffer.write(k.get_contents_as_string())
    # else:
    #     sys.stdout.write(k.get_contents_as_string())
