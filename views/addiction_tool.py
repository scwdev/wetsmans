from flask import Blueprint, render_template
from dotenv import load_dotenv

import pandas as pd
from pprint import pprint as pp

# addiction_tool_bp = Blueprint('addiction_tool', __name__)

# load_dotenv()

# @addiction_tool_bp.route('/addiction_tool', methods=['GET'])
# def form(dr_name):
#     return render_template('addiction_tool.html')


# # get the snps
snp_file = '../miscfiles/GenEd_AE_SNPlist.csv'
snp_list = pd.read_csv(snp_file)

# # get starts and stops
gene_positions_dataframe = pd.read_csv('../miscfiles/AE_Gene_Positions.csv',
                                       header=0,
                                       dtype={'Gene':str, 'Chrom':str, 'GRCh37_start':int, 'GRCh37_end':int}
)
# gene_positions_dataframe = gene_positions_dataframe.rename(columns={'Unnamed: 0': 'Gene'})
gene_list = gene_positions_dataframe['Gene'].tolist()
print(f'The GenEd Addiction Education Report cointains {len(gene_list)} genes...')


# get external data and return a dataframe
print('I am loading your Ancestry file...')
file = '../miscfiles/MickeyMouse_rawdata.txt'
header_row = 18 ## TODO dynamically determine header etc
dataframe = pd.read_csv(file,
                        header=header_row,
                        sep='\t',
                        dtype={'rsid':str, 'chromosome':str, 'position':int, 'chromosome':str,'allele1':str, 'allele2':str})
# print(f'Your file has {dataframe.shape[0]} data points.')
pp(dataframe)

# determine gender
# print('I am determinine your gender...')
# gender_dataframe = dataframe.loc[dataframe['chromosome'].isin(['23','X'])].reset_index()
# # pp(gender_dataframe)
# # gender = 'female'
# for i in range(0, 1000, 1):
#     #TODO merge allele1 and allele2 into "genotype"
#     gt = gender_dataframe.loc[i, 'allele1'+'allele2']
#     pp(gt)
#     if len(gt) > 1:
#         pass
#     else:
#         gender = 'male'
#         break
# print(f'You are genetically {gender}.')


# # filter on panel
# print('I am filtering out all the data that is outside the AE panel...')
# panel = pd.DataFrame()
# for gene in gene_list:
#     # print(gene)
#     temp = gene_dataframe[gene_dataframe['Gene'] == gene]
#     temp.reset_index(inplace=True, drop=True)
#     chrom = temp.loc[0, 'Chrom']
#     start = temp.loc[0, 'GRCh37_start']
#     end = temp.loc[0, 'GRCh37_end']
#     temp_dataframe = dataframe[dataframe['chromosome'] == chrom]
#     temp_dataframe = temp_dataframe[temp_dataframe['position'] >= start]
#     temp_dataframe = temp_dataframe[temp_dataframe['position'] <= end]
#     panel = panel.append(temp_dataframe)
#     # print()
# panel.reset_index(inplace=True, drop=True)

# panel.position = panel.position.astype(str)
# print(f'You have {panel.shape[0]} data points from 23andme in the AE panel...')





#########################TODO

# def Get_Index(dataframe, col, value):
#     i = dataframe.index[dataframe[col] == value].tolist()
#     if len(i) > 0:
#         index = i[0]
#         return index
#     else:
#         return None

# def findkeys(node, key_value):
#     if isinstance(node, list):
#         for i in node:
#             for x in findkeys(i, key_value):
#                 yield x
#     elif isinstance(node, dict):
#         if key_value in node:
#             yield node[key_value]
#         for j in node.values():
#             for x in findkeys(j, key_value):
#                 yield x

# # we need a precalculated way to take someone's 23andme or ancestry
# # data and return a standardized GenEd.csv
# # It needs to determine:
#     # company of origin
#     # Version
#     # correct inumbers
#     # correct indel references
#     # remake csv in vcf form for vep

# # This script doesn't do this in as modular a way as I'd like but it
# # has some modular functions in tit that can be used,



#########################TODO



# # remove no calls
# print('I am removing those positions where 23andme did not find any data...')
# panel = panel[~panel['genotype'].str.contains('-')]

# print(f'There are {panel.shape[0]} data points at which 23andme found information.')

# # replace inumbers with rsIDs where possible
# print('23andme uses some non-standard names for some of their data called inumbers.')
# print('I am finding standard identifiers for all of the inumbers I can...')
# conversion_file = 'rsid_to_inumber.csv'
# con_dataframe = pd.read_csv(conversion_file, dtype=str)
# con_dataframe = con_dataframe[con_dataframe['ID'].str.contains('rs')]
# con_dataframe = con_dataframe[con_dataframe['23andme'].str.contains('i')]
# con_dataframe = con_dataframe.drop_duplicates('23andme')

# with_rsid = panel[panel['# rsid'].str.contains('rs')]
# with_i = panel[panel['# rsid'].str.contains('i')]
# iss = con_dataframe['23andme'].tolist()
# with_i = with_i[with_i['# rsid'].isin(iss)]
# with_i['# rsid'] = with_i['# rsid'].map(con_dataframe.set_index('23andme')['ID'])

# # filter out inumbers
# print('I am filtering out the inumbers that I coud not replace...')
# with_i = with_i[with_i['# rsid'].str.contains('rs')]
# with_i = with_i.drop_duplicates('# rsid')

# # recombine all with rsid
# panel = with_rsid.append(with_i)
# print(f'There are {panel.shape[0]} data points remaining.')

# # handle indels
# indels = panel[panel['genotype'].str.contains('I|D')]
# print(indels)

# indel_refs = pd.read_csv('AE_23andme_Indels.csv')
# print(indel_refs)

# # delete the known wonky ones
# delete = indel_refs[indel_refs['alt'] == 'Delete']['# rsid'].tolist()
# panel = panel[~panel['# rsid'].isin(delete)]
# print(
#     f'After deleting indels that were not precisely defined we have {panel.shape[0]} data points left.')


# # add referece data
# print('I am getting reference data for these positions...')
# ref_dataframe = pd.read_csv('AE_23andMe_References.csv')
# ref_dataframe['location'] = ref_dataframe['chromosome']+':'+ref_dataframe['position'].astype(str)
# ref_dataframe.drop(['# rsid', 'chromosome', 'position'], axis=1, inplace=True)
# ref_dataframe.set_index('location', inplace=True, drop=True)

# print('I am comparing your data to the genomic reference build...')
# panel['location'] = panel['chromosome']+':'+panel['position']
# panel = pd.merge(panel, ref_dataframe, how='left', on='location')
# panel['ref'] = panel['reference']
# panel['reference'] = panel.reference*panel.genotype.str.len()
# panel = panel[panel['genotype'] != panel['reference']]
# print(f'You have {panel.shape[0]} data points in the AE panel at which you are not wild type.')
# panel.reset_index(inplace=True, drop=True)
# print(indel_refs.columns)


# # put in indel references
# for idx, row in indel_refs.iterrows():
#     rsid = indel_refs.loc[idx, '# rsid']
#     indel_ref = indel_refs.loc[idx, 'ref']
#     indel_ref_23andme = indel_refs.loc[idx, 'ref_23andme']
#     indel_alt = indel_refs.loc[idx, 'alt']
#     indel_alt_23andme = indel_refs.loc[idx, 'alt_23andme']
#     index = Get_Index(panel, '# rsid', rsid)
#     if index == None:
#         pass
#     else:
#         gt = panel.loc[index, 'genotype']
#         new_gt = gt.replace(indel_ref_23andme, indel_ref)
#         new_gt = new_gt.replace(indel_alt_23andme, indel_alt)
#         panel.loc[index, 'genotype'] = new_gt
#         panel.loc[index, 'ref'] = indel_ref
#         panel.loc[index, 'reference'] = indel_ref+indel_ref


# # unaccounted for indels
# unaccounted_indels = panel[panel.genotype.str.contains('I|D')]
# if unaccounted_indels.shape[0] > 0:
#     print(
#         f'There are {unaccounted_indels.shape[0]} inserts and deletions for which we lack reference alleles.')
#     print('We will look those up and add to our database. Be sure to check back in a few days.')
#     # send accounted_indels to a script that looks up refs
#     # ensembl_url = f"https://api.ncbi.nlm.nih.gov/variation/v0/refsnp/{pmrsid}/"
# print(panel)
# # determine alts
# panel.reset_index(inplace=True, drop=True)
# print('I am determineing your alternate allels...')
# for idx, row in panel.iterrows():
#     gt = panel.loc[idx, 'genotype']
#     print(idx, gt, gt[0])
#     ref = panel.loc[idx, 'ref']
#     try:
#         alt = gt.strip(ref)[0]
#     except IndexError:
#         alt = gt[0]
#     panel.loc[idx, 'alt'] = alt

# # turn dataframe into vcf
# print('Writing your VeP input file...')
# with open(f'{name}_23andme.vcf', 'w') as f:
#     f.write('##fileformat=VCFv4.2\n')
#     f.write('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tGT\n')
#     for idx, row in panel.iterrows():
#         gt = panel.loc[idx, 'genotype']
#         ref = panel.loc[idx, 'ref']
#         try:
#             alt = gt.strip(ref)[0]
#         except IndexError:
#             alt = gt[0]
#         chrom = panel.loc[idx, 'chromosome']
#         pos = panel.loc[idx, 'position']
#         f.write(f'{chrom}\t{pos}\t.\t{ref}\t{alt}\t.\t.\tGT\t0|1\n')
# print(f'I have written your VEP input file to {name}_23andme.vcf')


# ##############################################################
# # at this point the output needs to be put on the vep server and run
# # through VCF_To_VEP_v1S.py and then the output handled below
# ##############################################################


# # get vep for entire list
# vep_file = 'vcf_vep_output'

# # get vep output csv


# def Get_Header(file):
#     with open(file, 'r') as f:
#         lines = f.readlines()
#         count = 0
#         for i in range(len(lines)):
#             if '##' in lines[i]:
#                 count = count+1
#     return count


# def VEP_VCF_To_CSV(vcf, output_file):
#     header = Get_Header(vcf)
#     dataframe = pd.read_csv(vcf, sep='\t', header=header)
#     dataframe = dataframe[dataframe['CANONICAL'] == 'YES']
#     # dataframe = dataframe[dataframe['Consequence']!='downstream_gene_variant']
#     # dataframe = dataframe[dataframe['Consequence']!='upstream_gene_variant']
#     dataframe['SIFT_score'] = dataframe['SIFT'].str.extract('.*\((.*)\).*')
#     dataframe['PolyPhen_score'] = dataframe['PolyPhen'].str.extract('.*\((.*)\).*')
#     dataframe = dataframe[dataframe['SYMBOL'].isin(gene_list)]
#     dataframe.to_csv('MickeyMouseData_VEP.csv', index=False)


# file = 'vcf_vep_output.txt'
# VEP_VCF_To_CSV(file, 'MickeyMouseData_VEP.csv')
# vep_dataframe = pd.read_csv('MickeyMouseData_VEP.csv', dtype=str)
# vep_dataframe.drop_duplicates(['#Uploaded_variation', 'Consequence'], inplace=True)
# print(f'We have information on {vep_dataframe.shape[0]} variants to tell you about.')

# vep_dataframe.drop(['MANE_PLUS_CLINICAL', 'Feature_type', 'DISTANCE',
#              'FLAGS', 'SYMBOL_SOURCE', 'HGNC_ID', 'CANONICAL',
#              'MANE_SELECT', 'APPRIS', 'TSL', 'SWISSPROT', 'TREMBL',
#              'UNIPARC', 'UNIPROT_ISOFORM', 'GENE_PHENO', 'SOMATIC',
#              'PHENO', 'MOTIF_NAME', 'MOTIF_POS', 'HIGH_INF_POS',
#              'MOTIF_SCORE_CHANGE', 'TRANSCRIPTION_FACTORS'],
#             axis=1, inplace=True)
# print(vep_dataframe)

# for idx, row in vep_dataframe.iterrows():
#     print(vep_dataframe.loc[idx, 'ENSP'],
#           vep_dataframe.loc[idx, 'INTRON'], vep_dataframe.loc[idx, 'Consequence'])
# print(vep_dataframe.columns)
# time1 = time.time()
# print(time1-time0)