import sys
import hashlib
import os
import shutil
import zipfile


class HashFile:
    def md5(self):
        buf_size = 65536

        md5 = hashlib.md5()

        with open(self, 'rb') as f:
            while True:
                data = f.read(buf_size)
                if not data:
                    break
                md5.update(data)

        md5.update(data)
        # print("MD5: {0}".format(md5.hexdigest()))
        return md5.hexdigest()

    def sha1(self):
        buf_size = 65536

        sha1 = hashlib.sha1()

        with open(self, 'rb') as f:
            while True:
                data = f.read(buf_size)
                if not data:
                    break
                sha1.update(data)

        sha1.update(data)
        # print("SHA1: {0}".format(sha1.hexdigest()))
        return sha1.hexdigest()

    def save(hash, path):
        print('hash', hash)
        try:
            os.mkdir('store/' + str(hash[:2]))
        except:
            pass

        splitpath = path.split('/')
        splitpath = splitpath[-1].split('.')

        copypath = shutil.copy(path, 'store/' + str(hash[:2]) + '/' + hash + '.' + splitpath[1])

        # jungle_zip = zipfile.ZipFile('store/' + hash[:2] + '/' + hash + '.zip', 'w')
        # jungle_zip.write('store/' + str(hash[:2]) + '/' + hash + '.' + splitpath[1], compress_type=zipfile.ZIP_DEFLATED)
        # jungle_zip.close()

        print('copypath', copypath)

        return copypath

    def search(hashname):
        clip = hashname[:2]
        if os.path.exists('store/' + clip):
            print('Ok')
            dirfile = os.listdir('store/' + clip)
            print('dirfile', dirfile)

            for file in dirfile:
                print(hashname, file.split('.')[0])
                if hashname == file.split('.')[0]:
                    print('super, file is:', file)
                    print('pathfile', 'store/' + clip + '/' + file)
                    return 'store/' + clip + '/' + file

        print('return None')
        return None

    # def download(filepath):
    #     return
    #     pass

    def delete(filepath):
        os.remove(filepath)


# HashFile.search('5f6ef9cc177fa5ed76c66dfdf693df4769fb707f')