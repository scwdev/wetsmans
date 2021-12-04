from flask import Blueprint, render_template
from dotenv import load_dotenv

addiction_tool_bp = Blueprint('addiction_tool', __name__)

load_dotenv()

@addiction_tool_bp.route('/addiction_tool', methods=['GET'])
def form(dr_name):
    return render_template('addiction_tool.html')




# import pandas as pd
# import time


# def Get_Index(df, col, value):
#     i = df.index[df[col] == value].tolist()
#     if len(i) > 0:
#         index = i[0]
#         return index
#     else:
#         return None

# def findkeys(node, kv):
#     if isinstance(node, list):
#         for i in node:
#             for x in findkeys(i, kv):
#                 yield x
#     elif isinstance(node, dict):
#         if kv in node:
#             yield node[kv]
#         for j in node.values():
#             for x in findkeys(j, kv):
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

# time0 = time.time()

# # get the snps
# snp_file = 'GenEd_AE_SNPlist.csv'
# snp_list = pd.read_csv(snp_file)

# # get starts and stops
# gene_df = pd.read_csv('AE_Gene_Positions.csv')
# gene_df = gene_df.rename(columns={'Unnamed: 0': 'Gene'})
# gene_df['GRCh37_start'] = gene_df['GRCh37_start'].astype(int)
# gene_df['GRCh37_end'] = gene_df['GRCh37_end'].astype(int)
# gene_df['Chrom'] = gene_df['Chrom'].astype(str)
# gene_list = gene_df['Gene'].tolist()
# print(f'The GenEd Addiction Education Report cointains {len(gene_list)} genes...')


# # get external data and return a df
# print('I am loading your 23andme file...')
# # file = 'MickeyMouseData.txt'

# name = file.strip('.txt')
# file = 'Genome_John_Silver.txt'
# # file = 'Genome_Chicken_Little.txt'
# # file = 'Genome_Bugs_Bunny.txt'
# # file = 'DonaldDuck.txt'

# df = pd.read_csv(file, sep='\t', dtype=str)
# df['position'] = df['position'].astype(int)
# df['chromosome'] = df['chromosome'].astype(str)
# # print('original',df)
# print(f'Your file has {df.shape[0]} data points.')

# # determine gender
# print('I am determinine your gender...')
# gender_df = df[df['chromosome'] == 'X']
# gender_df.reset_index(inplace=True, drop=True)
# gender = 'female'
# for i in range(0, 1000, 1):
#     gt = gender_df.loc[i, 'genotype']
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
#     temp = gene_df[gene_df['Gene'] == gene]
#     temp.reset_index(inplace=True, drop=True)
#     chrom = temp.loc[0, 'Chrom']
#     start = temp.loc[0, 'GRCh37_start']
#     end = temp.loc[0, 'GRCh37_end']
#     temp_df = df[df['chromosome'] == chrom]
#     temp_df = temp_df[temp_df['position'] >= start]
#     temp_df = temp_df[temp_df['position'] <= end]
#     panel = panel.append(temp_df)
#     # print()
# panel.reset_index(inplace=True, drop=True)

# panel.position = panel.position.astype(str)
# print(f'You have {panel.shape[0]} data points from 23andme in the AE panel...')


# # remove no calls
# print('I am removing those positions where 23andme did not find any data...')
# panel = panel[~panel['genotype'].str.contains('-')]

# print(f'There are {panel.shape[0]} data points at which 23andme found information.')

# # replace inumbers with rsIDs where possible
# print('23andme uses some non-standard names for some of their data called inumbers.')
# print('I am finding standard identifiers for all of the inumbers I can...')
# conversion_file = 'rsid_to_inumber.csv'
# con_df = pd.read_csv(conversion_file, dtype=str)
# con_df = con_df[con_df['ID'].str.contains('rs')]
# con_df = con_df[con_df['23andme'].str.contains('i')]
# con_df = con_df.drop_duplicates('23andme')

# with_rsid = panel[panel['# rsid'].str.contains('rs')]
# with_i = panel[panel['# rsid'].str.contains('i')]
# iss = con_df['23andme'].tolist()
# with_i = with_i[with_i['# rsid'].isin(iss)]
# with_i['# rsid'] = with_i['# rsid'].map(con_df.set_index('23andme')['ID'])

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
# ref_df = pd.read_csv('AE_23andMe_References.csv')
# ref_df['location'] = ref_df['chromosome']+':'+ref_df['position'].astype(str)
# ref_df.drop(['# rsid', 'chromosome', 'position'], axis=1, inplace=True)
# ref_df.set_index('location', inplace=True, drop=True)

# print('I am comparing your data to the genomic reference build...')
# panel['location'] = panel['chromosome']+':'+panel['position']
# panel = pd.merge(panel, ref_df, how='left', on='location')
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

# # turn df into vcf
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
#     df = pd.read_csv(vcf, sep='\t', header=header)
#     df = df[df['CANONICAL'] == 'YES']
#     # df = df[df['Consequence']!='downstream_gene_variant']
#     # df = df[df['Consequence']!='upstream_gene_variant']
#     df['SIFT_score'] = df['SIFT'].str.extract('.*\((.*)\).*')
#     df['PolyPhen_score'] = df['PolyPhen'].str.extract('.*\((.*)\).*')
#     df = df[df['SYMBOL'].isin(gene_list)]
#     df.to_csv('MickeyMouseData_VEP.csv', index=False)


# file = 'vcf_vep_output.txt'
# VEP_VCF_To_CSV(file, 'MickeyMouseData_VEP.csv')
# vep_df = pd.read_csv('MickeyMouseData_VEP.csv', dtype=str)
# vep_df.drop_duplicates(['#Uploaded_variation', 'Consequence'], inplace=True)
# print(f'We have information on {vep_df.shape[0]} variants to tell you about.')

# vep_df.drop(['MANE_PLUS_CLINICAL', 'Feature_type', 'DISTANCE',
#              'FLAGS', 'SYMBOL_SOURCE', 'HGNC_ID', 'CANONICAL',
#              'MANE_SELECT', 'APPRIS', 'TSL', 'SWISSPROT', 'TREMBL',
#              'UNIPARC', 'UNIPROT_ISOFORM', 'GENE_PHENO', 'SOMATIC',
#              'PHENO', 'MOTIF_NAME', 'MOTIF_POS', 'HIGH_INF_POS',
#              'MOTIF_SCORE_CHANGE', 'TRANSCRIPTION_FACTORS'],
#             axis=1, inplace=True)
# print(vep_df)

# for idx, row in vep_df.iterrows():
#     print(vep_df.loc[idx, 'ENSP'],
#           vep_df.loc[idx, 'INTRON'], vep_df.loc[idx, 'Consequence'])
# print(vep_df.columns)
# time1 = time.time()
# print(time1-time0)