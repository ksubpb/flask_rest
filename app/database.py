import sys
import csv

class ZipCode:
    def __init__(self, zipcode, pref, address, address_yomi):
        self.code = zipcode
        self.pref = pref
        self.address = address
        self.address_yomi = address_yomi

    def to_json(self):
        return {
            "zipcode": self.code,
            "pref": self.pref,
            "address": self.address,
            "address_yomi": self.address_yomi
        }

class ZipCodeBuilder:
    def build(self, filename):
        self._zipcodes = {}
        with open(filename, "r") as f:
            reader = csv.reader(f)
            for rows in reader:
                zc = self._parse_each(rows)
                self._zipcodes[zc.code] = zc
        return self._zipcodes

    def _parse_each(self, rows):
        zipcode = rows[2].strip("\"")
        pref = rows[6].strip("\"")
        address = rows[7].strip("\"") + rows[8].strip("\"")
        address_yomi = rows[4].strip("\"") + rows[5].strip("\"")
        return ZipCode(int(zipcode), pref, address, address_yomi)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: python database.py <zipcode db> <zipcode...>")
    else:
        db = ZipCodeBuilder().build(sys.argv[1])
        print(f"read {len(db)} records")
        for zc in sys.argv[2:]:
            zc = int(zc)
            if zc in db:
                print(db[zc].to_json())
            else:
                print(f"{zc}: not found")
        assert db[6590016].pref == "兵庫県", "6590016 の県は兵庫県であるはずです"
        print(db[6150042].to_json())

