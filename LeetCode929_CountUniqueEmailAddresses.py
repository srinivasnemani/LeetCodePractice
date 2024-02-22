
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unqems = dict()
        for em in emails:
            [local_name, domain] = em.split(sep="@")
            split_words = local_name.split(sep="@")
            ln1 = split_words[0].split(sep="+")
            ln2 = ln1[0].replace(".", "")
            uniq_email = ln2 + "@" + domain
            counter = unqems.get(uniq_email, 0)
            if counter == 0:
                unqems[uniq_email] =  1
        if unqems:
            return sum(list(unqems.values()))
        else:
            return 0
