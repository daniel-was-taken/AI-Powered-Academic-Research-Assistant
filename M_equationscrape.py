import re

# text = "5.1.3PreprocessingthewebdataThedatathatweextractedfromthewebmaynotbeinaformatthatissuitableforfurtherprocesses.Inthisstep,wewillneedtocleanthedatabyremovinganyunwantedcharacters,correctinganyerrors,andconvertingthedataintoaconsistentformat5.1.4AbstractiveSummarisationATransformerisusedforabstractivesummarisation,specificallytheLongT5model.TheLongT5modelworksbyfirstencodingtheinputtextintoase-quenceoftokens.ThesetokensarethenpassedthroughtheTransformeren-coder,whichlearnstoidentifytherelationshipsbetweenthetokens.Theen-codedtokensarethenpassedthroughtheTransformerdecoder,whichgeneratestheoutputsummary.14Chapter5Design5.1.5SentenceRankingFindoutkeytakeawaysfromallthepapers.Thesekeytakeawaysgiveusanideaabouttheessentialsentencesfromthepapers.TextRankturnsouttobewellsuitedforthistypeofapplication,sinceitallowsforarankingovertextunitsthatisrecursivelycomputedbasedoninformationdrawnfromtheentiretext.[5]Formally,giventwosentencesSiandSj,withasentencebeingrepre-sentedbythesetofNiwordsthatappearinthesentence:Si=wi1,wi2,...,wiNi,Similarity(Si,Sj)=|wk|wk∈Si&wk∈Sj|log(|Si|)+log(|Sj|)(5.1)Thescoreiscalculatedforallsentencesusing,Score(s)=d+sum(Score(t)∗Similarity(s,t))(5.2)Where,Score(s)isthescoreofsentences,disadampingfactor,typicallysetto0.85,Score(t)isthescoreofsentencet,Similarity(s,t)isthesimilaritybetweensentencessandt.5.2PerformanceEvaluationParameters5.2.1Recall-OrientedUnderstudyforGistingEvaluation(ROUGE)ScoreTheROUGEscoreisusedtoevaluatethequalityofmachinetranslationoutputs."
input_file = 'text/textcontent.txt'

with open(input_file,'r',encoding='utf-8') as file:
    text = file.read()


# Define a regex pattern to match equations
equation_pattern = r"\(.*?\)\(\d+\.\d+\)"

# Find all equations in the text
equations = re.findall(equation_pattern, text)

# Print the extracted equations


output_file = 'text/equation.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    for equation in equations:
        file.write(equation)
    
