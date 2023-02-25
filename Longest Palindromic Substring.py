#!/usr/bin/env python
# coding: utf-8

# In[33]:


# Longest Palindromic Substring

# Given a string s, return the longest 
# palindromic
 
# substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
s='wsgdzojcrxtfqcfkhhcuxxnbwtxzkkeunmpdsqfvgfjhusholnwrhmzexhfqppatkexuzdllrbaxygmovqwfvmmbvuuctcwxhrmepxmnxlxdkyzfsqypuroxdczuilbjypnirljxfgpuhhgusflhalorkcvqfknnkqyprxlwmakqszsdqnfovptsgbppvejvukbxaybccxzeqcjhmnexlaafmycwopxntuisxcitxdbarsicvwrvjmxsapmhbbnuivzhkgcrshokkioagwidhmfzjwwywastecjsolxmhfnmgommkoimiwlgwxxdsxhuwwjhpxxgmeuzhdzmuqhmhnfwwokgvwsznfcoxbferdonrexzanpymxtfojodcfydedlxmxeffhwjeegqnagoqlwwdctbqnuxngrgovrjesrkjrfjawknbrsfywljscfvnjhczhyeoyzrtbkvvfvofykkwoiclgxyaddhpdoztdhcbauaagjmfzkkdqexkczfsztckdlujgqzjyuittnudpldjvsbwbzcsazjpxrwfafievenvuetzcxynnmskoytgznvqdlkhaowjtetveahpjguiowkiuvikwewmgxhgfjuzkgrkqhmxxavbriftadtogmhlatczusxkktcsyrnwjbeshifzbykqibghmmvecwwtwdcscikyzyiqlgwzycptlxiwfaigyhrlgtjocvajcnqyenxrnjgogeqtvkxllxpuoxargzgcsfwavwbnktchwjebvwwhfghqkcjhuhuqwcdsixrkfjxuzvhjxlyoxswdlwfytgbtqbeimzzogzrlovcdpseoafuxfmrhdswwictsctawjanvoafvzqanvhaohgndbsxlzuymvfflyswnkvpsvqezekeidadatsymbvgwobdrixisknqpehddjrsntkqpsfxictqbnedjmsveurvrtvpvzbengdijkfcogpcrvwyf'
if s==s[::-1]:
    print( s)
else:
    l = []
    for i in range(len(s)+1):
        for j in range(i):
            a = (s[j:i])
            if a==a[::-1]:
                l.append(a)
            
    l.sort(key=len)
    print( l[-1])


# In[ ]:





# In[30]:





# In[ ]:




