from django.db import models
from django.utils import timezone

import json

class Preference(models.Model):
    allowedFactions = models.TextField(default="{}")


class Faction(models.Model):
    tId = models.IntegerField(default=0, unique=True)
    name = models.CharField(default="MyFaction", max_length=200)
    hitsThreshold = models.IntegerField(default=100)

    lastAPICall = models.IntegerField(default=0)
    nAPICall = models.IntegerField(default=2)

    # "login1:key1,login2:key2,login3:key3"
    apiString = models.TextField(default="{}")  # for 10 pairs login(15):key(16)

    def __str__(self):
        return "{} [{}]".format(self.name, self.tId)
    #
    # def get_n_chains(self):
    #     return(len(self.chain_set.all()))
    #
    # def get_random_key(self):
    #     from numpy.random import randint
    #     pairs = self.apiString.split(",")
    #     i = randint(0, len(pairs))
    #     return pairs[i].split(":")
    #
    # def get_all_pairs(self):
    #     if str(self.apiString) == "0" or self.apiString == "":
    #         return []
    #     else:
    #         pairs = self.apiString.split(",")
    #         return [pair.split(":") for pair in pairs]
    #
    # def get_all_keys(self):
    #     if str(self.apiString) == "0" or self.apiString == "":
    #         return []
    #     else:
    #         pairs = self.apiString.split(",")
    #         return [pair.split(":")[1] for pair in pairs]
    #
    # def toggle_key(self, name, key):
    #     print("[MODEL toggle_key] " + name)
    #     pairs = self.get_all_pairs()
    #     if key in self.get_all_keys():
    #         print("[MODEL toggle_key] remove key")
    #         pairs.remove([name, key])
    #     else:
    #         print("[MODEL toggle_key] add key")
    #         if len(pairs) < 11:
    #             pairs.append([name, key])
    #         else:
    #             return False
    #
    #     string = ",".join([p[0] + ":" + p[1] for p in pairs])
    #     self.apiString = string if string else 0
    #     self.save()
    #
    #     return True
    #
    # def add_key(self, name, key):
    #     print("[models.chain.add_key] " + name)
    #     pairs = self.get_all_pairs()
    #     if key not in pairs:
    #         if len(pairs) < 11:
    #             print("[models.chain.add_key] add key")
    #             pairs.append([name, key])
    #         else:
    #             print("[models.chain.add_key] too many key saved")
    #             return False
    #     else:
    #         print("[models.chain.add_key] kee already saved")
    #         return False
    #
    #     string = ",".join([p[0] + ":" + p[1] for p in pairs])
    #     self.apiString = string if string else 0
    #     self.save()
    #
    #     return True

    def addKey(self, id, key):
        keys = json.loads(self.apiString)
        keys[str(id)] = key
        self.apiString = json.dumps(keys)
        self.save()

    def delKey(self, id):
        keys = json.loads(self.apiString)
        if str(id) in keys:
            del keys[str(id)]
        self.apiString = json.dumps(keys)
        self.save()

    def getRadomKey(self):
        import random
        keys = json.loads(self.apiString)
        return random.choice(list(keys.items()))

    def getAllPairs(self):
        keys = json.loads(self.apiString)
        return list(keys.items())

    def numberOfReportsToCreate(self):
        return len(self.chain_set.filter(createReport=True))

    def liveChain(self):
        return bool(self.chain_set.filter(tId=0))

class Chain(models.Model):
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    tId = models.IntegerField(default=0)
    reportNHits = models.IntegerField(default=0)
    nHits = models.IntegerField(default=1)
    nAttacks = models.IntegerField(default=1)
    respect = models.FloatField(default=0)
    start = models.IntegerField(default=0)
    end = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    createReport = models.BooleanField(default=False)
    jointReport = models.BooleanField(default=False)
    graph = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return "chain [{}]".format(self.tId)

    def have_report(self):
        return True if len(self.report_set.all()) else False

    def toggle_report(self):
        self.jointReport = not self.jointReport
        return self.jointReport


class Member(models.Model):
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    tId = models.IntegerField(default=0, unique=True)
    name = models.CharField(default="Duke", max_length=15)
    daysInFaction = models.IntegerField(default=0)
    lastAction = models.CharField(default="-", max_length=200)

    def __str__(self):
        return "{} [{}]".format(self.name, self.tId)


class Report(models.Model):
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return("Report of {}".format(self.chain))


class Bonus(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    tId = models.IntegerField(default=0)
    name = models.CharField(default="Duke", max_length=64)
    hit = models.IntegerField(default=0)
    respect = models.FloatField(default=0)
    respectMax = models.FloatField(default=0)

    def __str__(self):
        return("Bonus of {}".format(self.report.chain))


class Count(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    attackerId = models.IntegerField(default=0)
    name = models.CharField(default="Duke", max_length=64)
    hits = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    respect = models.FloatField(default=0)
    fairFight = models.FloatField(default=0)
    war = models.FloatField(default=0)
    retaliation = models.FloatField(default=0)
    groupAttack = models.FloatField(default=0)
    overseas = models.FloatField(default=0)
    daysInFaction = models.IntegerField(default=0)
    beenThere = models.BooleanField(default=False)
    graph = models.TextField(default="", null=True, blank=True)
    watcher = models.FloatField(default=0)

    def __str__(self):
        return("Count of {}".format(self.report.chain))


class Attacks(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    tss = models.IntegerField(default=0)
    tse = models.IntegerField(default=0)
    req = models.TextField()


class Crontab(models.Model):
    id = models.AutoField(primary_key=True)
    faction = models.ManyToManyField(Faction, blank=True)

    def __str__(self):
        return "Crontab #{}".format(self.id)

    def nFactions(self):
        return len(self.faction.all())
