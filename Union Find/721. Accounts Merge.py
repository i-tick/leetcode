from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        par = [i for i in range(n)]

        def find(i):
            if i!=par[i]:
                par[i] = find(par[i])
            return par[i]
        
        def union(i,j):
            p1 = find(i)
            p2 = find(j)
            if p1!=p2:
                par[max(p1,p2)] = min(p1, p2)

        # Create a mapping of email to account index
        # and union accounts based on shared emails
        # acc_dict will map each email to the account index it belongs to
        # If an email appears in multiple accounts, we union those accounts
        # acc_dict will store the email as key and the account index as value
        # We will use union-find to group accounts by their emails
        # par will store the parent of each account index
        # find will find the root parent of an account index
        # union will connect two account indices
        # accounts is a list of lists where each sublist contains an account name followed by its emails
        acc_dict = {}
        for i, l in enumerate(accounts):
            name = l[0]
            for j in range(1, len(l)):
                if l[j] in acc_dict:
                    union(acc_dict[l[j]], i)
                acc_dict[l[j]] = i
        
        # Merge accounts based on the union-find structure
        # merged_acc will store the emails grouped by their root account index
        # We will create a new list where each element is a list containing the account name and sorted emails
        # We will iterate through acc_dict and find the root parent for each account index
        # and append the email to the corresponding list in merged_acc
        # Finally, we will create a new list where each element is a list containing the account name and sorted emails
        # The final result will be a list of lists where each sublist contains the account name followed by its emails
        # The final result will be sorted by account name and emails
        # We will use a defaultdict to group emails by their root account index
        # acc_dict will map each email to the account index it belongs to
        # merged_acc will map each account index to a list of emails
        merged_acc = defaultdict(list)
        for email, id in acc_dict.items():
            merged_acc[find(id)].append(email)
        
        final_merge = []
        for id, emails in merged_acc.items():
            final_merge.append([accounts[id][0]] + sorted(emails))
        return final_merge
