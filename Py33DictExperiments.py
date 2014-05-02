import dictinfo2

def pythonDict():
    """
    pmap looks like ``{key: [slot, slot, slot], ...}``.
    """
    pmap = {}

    with open("TaleOfTwoCities.txt", mode='r', encoding='utf-8') as f:
        words = (word for line in f for word in line.split() if len(word) > 7)
        pmap = dictinfo2.probe_all_steps(words)
    return pmap

def countProbes(pmap):
    """
    count number of probes for each key
    """
    probes = {}
    for key in pmap:
        probes[key] = len(pmap[key])
    return probes

############################################# 
if __name__ == "__main__":

    from visualizerAccumulator import VisualAnalyzer
    
    a = VisualAnalyzer(13525, 12, title="Python 3.3 dictionary")
    pmap = pythonDict()
    probes = countProbes(pmap)

    # plot data
    with open("TaleOfTwoCities.txt", mode='r', encoding='utf-8') as f:
        words = (word for line in f for word in line.split() if len(word) > 7)
        for key in words:
            number_of_probes = probes[key]
            a.addDataValue(number_of_probes)

    a.plotData()