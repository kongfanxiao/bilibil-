#-*-coding:GBK -*- 
from dataclasses import replace
from string import printable
from shutil import copyfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shutil
import os
import sys
import glob
from PIL import Image
import time

path = 'D:/1007private/anime/漫画/bilibili/'
dir_name = '虚构推理'
list_path = path + dir_name#原文件夹列表    0文件夹
new_list_path = list_path + '1'  #1文件夹
num_i = 0
list_path2 = list_path + '2'#新目录                                    2文件夹

def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在 true
    # 不存在 false
    isExits = os.path.exists(path)

    # 判断结果
    if not isExits:
        os.makedirs(path)  # 不存在则创建该目录
        print(path + " 创建成功")
        return True
    else:
        print(path + " 目录已经存在")
        return False

def del_files(dir_path):
    if os.path.isfile(dir_path):
        try:
            os.remove(dir_path)
        except BaseException as e:
            print(e)
    elif os.path.isdir(dir_path):
        file_lis = os.listdir(dir_path)
        for file_name in file_lis:
            tf = os.path.join(dir_path,file_name)
            del_files(tf)
    print('ok')


def jiema(x):
    aaa = {'[':'','{':'',']':'','}':'','"':'','"':'',':':'',',':'','"':'','[':'',']':''}
    
    n = ''
    for i in x:
        if i in aaa.keys():
            i = aaa[i]
        n += str(i)
    return n


word_dic = {',"videoPath":null,"videoSize":null':'','"path":"https://manga.hdslb.com/bfs/manga/':''}


for root, dirs, files in os.walk(list_path):       #将ind.dat转化为ind.txt
    file_list_trans = list(files)
    for i_dat in range(len(file_list_trans)):
        if file_list_trans[i_dat][-3:] == 'dat':
            root_dat = root + '/' + file_list_trans[i_dat]
            root_dat1 = root + '/index.txt'
            shutil.copyfile(root_dat,root_dat1)    #copyfile(1,2)，将1复制到2，可修改文件名
i233 = 0   
df_index = pd.DataFrame()
for root, dirs, files in os.walk(list_path):        #处理ind.txt中的文字，只剩下图片名的顺序
    index_root = root + '/ind.txt'
    root_list = list(root)
    file_list_trans = list(files)
    for i_txt in range(len(file_list_trans)):
        pic_index = []
        if file_list_trans[i_txt][-3:] == 'dat':
            old_path = root + '/' + file_list_trans[i_txt]
            new_path = root + '/' + file_list_trans[i_txt].replace('dat','txt')
            copyfile(old_path,new_path)
        if file_list_trans[i_txt][-3:] == 'txt':
            root_txt = root + '/' + file_list_trans[i_txt]
            with open(root_txt) as f:
                for line in f:
                    f_str = str(line)
            f_pic = jiema(f_str)
            f_pic1 = f_pic.replace('videoPathnullvideoSizenull','')
            f_pic2 = f_pic1.replace('pathhttps//manga.hdslb.com/bfs/manga/','')
            num_word = f_pic2.count('jpg')
            xy_num = []
            for word_x in range(len(f_pic2)):
                if (f_pic2[word_x:word_x+3] == 'jpg'):
                    ias = word_x + 3
                    xy_num.append(ias)
            xy_num1 = xy_num
            xy_num.insert(0,0)
            i2 = 0
            for word_x in range(len(xy_num)-1):
                if i2 == 0:
                    pic_index.append(f_pic2[xy_num[i2]:xy_num[i2+1]])
                elif i2 > 0:
                    pic_index.append(f_pic2[(xy_num[i2]+10):xy_num[i2+1]])
                i2 = i2 + 1
            if os.path.exists(index_root):
                os.remove(index_root)
            with open(index_root,'a') as f_ind:
                f_ind.write(str(pic_index))
            index_root1 = root[:-3] + 'ind.txt'
            copyfile(index_root,index_root1)
for root, dirs, files in os.walk(list_path):        #删除int文件夹
    if root[-3:] == 'int':
        shutil.rmtree(root)
    if root == list_path:
        file_list_trans = list(files)
        for ijk in range(len(file_list_trans)):
            file_path = root + '/' + file_list_trans[ijk]
            os.remove(file_path)
for root, dirs, files in os.walk(list_path):        #将view后缀去掉，增加jpg文件
    file_list_trans2 = list(files)
    for i_txt in range(len(file_list_trans2)):
        if file_list_trans2[i_txt][-4:] == 'view':
            print(file_list_trans2[i_txt][:-5])
            old_path = root + '/' + file_list_trans2[i_txt]
            new_path = root + '/' + file_list_trans2[i_txt][:-5]
            shutil.copyfile(old_path,new_path)
for root, dirs, files in os.walk(list_path):        #将view后缀去掉
    file_list_trans3 = list(files)
    for i_txt in range(len(file_list_trans3)):
        if file_list_trans3[i_txt][-4:] == 'view':
            file_path1 = root + '/' + file_list_trans3[i_txt]
            os.remove(file_path1)
data_list1 = ['a','b']
data_list2 = []
for root, dirs, files in os.walk(list_path):
    file_list_trans3 = list(files)
    for i_txt in range(len(file_list_trans3)):
        if file_list_trans3[i_txt][-3:] == 'txt':
            txt_root = root + '/' + file_list_trans3[i_txt]
            with open(txt_root,encoding='utf-8') as file_txt:
                data_list = file_txt.read()                     #读取ind.txt文件
            data_list1 = list(data_list.split(','))
            data_list2 = list(data_list.split(','))
            for ikik in range(len(data_list1)):
                #print('len',len(data_list1[ikik]))
                i_s = 2                             #开始 
                i_e = len(data_list1[ikik]) - 1     #结束
                for ik in range(len(data_list1[ikik])):
                     if data_list1[ikik][ik-2] == 'j' and data_list1[ikik][ik-1] == 'p' and data_list1[ikik][ik] == 'g': #判断jpg位置
                        print('end',ik + 1)
                        i_e = ik + 1
                #print('data_list1[',ikik,'][',i_s,':',i_e,']',data_list1[ikik][i_s:(i_e)])
                data_list2[ikik] = data_list1[ikik][i_s:i_e]
            for root, dirs, files in os.walk(root):
                for ij in range(len(data_list2)):
                    old_path1 = root + '/' + data_list2[ij]
                    print('old_path',old_path1)
                    for i_txt1 in range(len(file_list_trans3)):
                        if file_list_trans3[i_txt1] == data_list2[ij]:
                            print(ij,'same          ',data_list2[ij],'           same')
                            if ij < 10:
                                ij_num = '000' + str(ij) + '.jpg'
                            elif ij < 100:
                                ij_num = '00' + str(ij) + '.jpg'
                            elif ij < 1000:
                                ij_num = '0' + str(ij) + '.jpg'
                            new_path1 = root + '/' + ij_num
                            print(new_path1)
                            shutil.copyfile(old_path1,new_path1)
                            os.remove(old_path1)


mkdir(new_list_path)
ijk = 0
for root, dirs, files in os.walk(list_path):
    print('*-+*-+*-+/*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*')
    file_list_trans4 = list(files)
    for l in range(len(file_list_trans4)):
        if file_list_trans4[l][-3:] == 'jpg':
            #print(file_list_trans4[l])
            old_path5 = root + '/' + file_list_trans4[l]
            if ijk < 10:
                l_txt1 = '0000' + str(ijk) + '.jpg'
            elif ijk < 100:
                l_txt1 = '000' + str(ijk) + '.jpg'
            elif ijk < 1000:
                l_txt1 = '00' + str(ijk) + '.jpg'
            elif ijk < 10000:
                l_txt1 = '0' + str(ijk) + '.jpg'
            new_path5 = new_list_path + '/' + l_txt1
            #print(l_txt1)
            shutil.copyfile(old_path5,new_path5)
            ijk = ijk + 1
            print('序号',ijk)
