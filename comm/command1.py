# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:06:14 2018

@author: wuzw
"""

from recommendations import critics
from math import sqrt

critics['Lisa Rose']
critics['Gene Seymour']

#欧几里得算法
def sim_distance(prefs,person1,person2):
    si={}
    for item in prefs[person1]:
        #print(item)
        if item in prefs[person2]:
            si[item] = 1
    
    if len(si)==0: return 0
    #print(si)
    
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) 
                       for item in prefs[person1] if item in prefs[person2]])
    
    return 1/(1+sqrt(sum_of_squares))

sim_distance(critics,'Lisa Rose','Gene Seymour')

#皮尔逊相关度评价
def sim_person(prefs,p1,p2):
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:si[item]=1
    
    n=len(si)
    
    if n==0:return 1
    
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])
    
    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
    
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
    
    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0:return 0
    
    
    #print(num,den)
    r=num/den
    return r

sim_person(critics,'Lisa Rose','Gene Seymour')


#为评论者打分
def topMatches(prefs,person,n=5,similarity=sim_person):
    scores=[(similarity(prefs,person,other),other) for other in prefs if other!=person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

topMatches(critics,'Toby',n=3)

topMatches(critics,'Gene Seymour',similarity=sim_distance)

def getRecommendations(prefs,person,similarity=sim_person):
    totals={}
    simSums={}
    for other in prefs:
        if other==person:continue
        sim=similarity(prefs,person,other)
        
        if sim <=0:continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item]==0:
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
                
                simSums.setdefault(item,0)
                simSums[item]+=sim
    
    print('totals',totals)
    print('simSums',simSums)
    rankings=[(total/simSums[item],item) for item,total in totals.items()]
    
    rankings.sort()
    rankings.reverse()
    return rankings

getRecommendations(critics,'Toby')

def transformPrefs(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{})
            
            result[item][person] = prefs[person][item]
    return result

movies=transformPrefs(critics)
print(movies)
topMatches(movies,'Lady in the Water',similarity=sim_distance)

def calculateSimilarItems(prefs,n=10):
    result={}
    itemPrefs = transformPrefs(prefs)
    #print(itemPrefs)
    c=0
    for item in itemPrefs:
        print(item)
        c+=1
        if c%100==0:print('%d/%d'%(c,len(itemPrefs)))
        scores=topMatches(itemPrefs,item,n=n,similarity=sim_distance)
        #print(scores)
        result[item]=scores
    return result

itemsim = calculateSimilarItems(critics)

def getRecommendedItems(prefs,itemMatch,user):
    userRations=prefs[user]
    scores={}
    totalSim={}
    
    for (item,rating) in userRations.items():
        for (similarity,item2) in itemMatch[item]:
        
            if item2 in userRations:continue
    
            scores.setdefault(item2,0)
            scores[item2]+=similarity*rating
            
            totalSim.setdefault(item2,0)
            totalSim[item2]+=similarity
    
    rankings=[(score/totalSim[item],item) for item,score in scores.items()]
    
    rankings.sort()
    rankings.reverse()
    return rankings

getRecommendedItems(critics,itemsim,'Toby')
