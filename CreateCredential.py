class createCredential:
    def __init__(self):
        pass
    @staticmethod
    def detailsCredential(datafile_link):
        # part 1
        aa = datafile_link
        aa1 = aa.split(".com")[0]
        aa2 = str(aa1)+".com"
        # print(aa2)

        # part 2
        local_file_name = aa.split("?")[0].split("/")[-1]
        # print(local_file_name)

        # part 3
        dd = aa.split("?")[0].split("/")[::-1]
        # print(dd)
        kk1 = []
        for i in dd:
            if len(i)<2:
                break
            kk1.append(i)
        pp = kk1[::-1]
        # print(pp)
        qq = "/".join(pp)
        dataset_url = str("/")+qq
        # print(dataset_url)

        # part 4
        mm = pp[:2]
        dp = []
        dp.append(aa2)
        for i in mm:
            dp.append(i)
        # mm.insert(aa2,0)
        site_url = "/".join(dp)
        # print(site_url)
        
        return [local_file_name, dataset_url, site_url]