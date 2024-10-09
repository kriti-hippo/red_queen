import os
import sys
sys.path.append(os.path.abspath('./utils'))

from normal_utils import *
from scenario_template import *
import pandas as pd
from tqdm import tqdm
import re
import ast
import numpy as np
import shutil
import json
import concurrent.futures
import argparse
from datasets import load_dataset
access_token = read_json_file('./utils/config.json')['hugging_face_token']  ### Add your hugging face token here
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
torch.set_grad_enabled(False)
turn_dict = {1:'compressed',3:'three', 4:'four', 5:'five'} 
template_list = ['occupation_teacher', 'occupation_police', 'occupation_detective', 'occupation_lawyer', 'occupation_priest', 'relation_friend', 'relation_neighbor', 'relation_someone', 'relation_relative', 'relation_son']
### Add your model id here
open_model_id_dict = {"meta-llama/Meta-Llama-3-8B-Instruct":'llama3_7b_{}_data.json',
                 "meta-llama/Meta-Llama-3-70B-Instruct":'llama3_70b_{}_data.json',
                 "meta-llama/Meta-Llama-3.1-70B-Instruct":'llama3_1_70b_{}_data.json',
                 "meta-llama/Meta-Llama-3.1-405B-Instruct":'llama3_1_405b_{}_data.json',
                "Qwen/Qwen2-7B-Instruct":'qwen2_7b_{}_data.json',
                "Qwen/Qwen2-72B-Instruct":'qwen2_72b_{}_data.json',
                "mistralai/Mixtral-8x7B-Instruct-v0.1":'mixtral_7b_{}_data.json',
                "mistralai/Mixtral-8x22B-Instruct-v0.1":'mixtral_22b_{}_data.json'
}

def attack_generation_data_open():
    attack_data_list_dict = {}
    for model_id in open_model_id_dict.keys():
        tokenizer = AutoTokenizer.from_pretrained(model_id,token=access_token)
        attack_data_list = []
        for key in harmful_dict.keys():
            sample_list = harmful_dict[key]
            for action in sample_list:
                for type_ in template_list:
                    for i in [1,3,4,5]:
                        temp_dict = {}
                        class_name = f"MultiTurnAttack_{type_}_{turn_dict[i]}_turn"
                        class_object = globals()[class_name]
                        mt = class_object()   
                        if i == 1:
                            messages = [
                                {"role": "system", "content": mt.system_prompt},
                                {"role": "user", "content": mt.sentence_1.format(action= action)},
                            ]
                        elif i == 3:
                            messages = [
                                {"role": "system", "content": mt.system_prompt},
                                {"role": "user", "content": mt.sentence_1.format(action= action)},
                                {"role": "assistant", "content": mt.response_1},
                                {"role": "user", "content": mt.sentence_2},
                                {"role": "assistant", "content": mt.response_2},
                                {"role": "user", "content": mt.sentence_3},
                            ]
                        elif i == 4:
                            messages = [
                                {"role": "system", "content": mt.system_prompt},
                                {"role": "user", "content": mt.sentence_1.format(action= action)},
                                {"role": "assistant", "content": mt.response_1},
                                {"role": "user", "content": mt.sentence_2},
                                {"role": "assistant", "content": mt.response_2},
                                {"role": "user", "content": mt.sentence_3},
                                {"role": "assistant", "content": mt.response_3},
                                {"role": "user", "content": mt.sentence_4},
                            ]
                        else:
                            messages = [
                                {"role": "system", "content": mt.system_prompt},
                                {"role": "user", "content": mt.sentence_1.format(action= action)},
                                {"role": "assistant", "content": mt.response_1},
                                {"role": "user", "content": mt.sentence_2},
                                {"role": "assistant", "content": mt.response_2},
                                {"role": "user", "content": mt.sentence_3},
                                {"role": "assistant", "content": mt.response_3},
                                {"role": "user", "content": mt.sentence_4},
                                {"role": "assistant", "content": mt.response_4},
                                {"role": "user", "content": mt.sentence_5},
                            ]
                        query = tokenizer.apply_chat_template(messages,tokenize=False)
                        temp_dict['action'] = action
                        temp_dict['query'] = query
                        temp_dict['turn'] = i
                        temp_dict['type'] = type_
                        temp_dict['category'] = key
                        attack_data_list.append(temp_dict)
                        attack_data_list_dict[open_model_id_dict[model_id].format("attack")] = attack_data_list

    return attack_data_list_dict


def attack_generation_data_closed(attack_data_list_dict):
    attack_data_list = []
    for key in harmful_dict.keys():
        sample_list = harmful_dict[key]
        for action in sample_list:
            for type_ in template_list:
                for i in [1,3,4,5]:
                    temp_dict = {}
                    class_name = f"MultiTurnAttack_{type_}_{turn_dict[i]}_turn"
                    class_object = globals()[class_name]
                    mt = class_object()   
                    if i == 1:
                        messages = [
                            {"role": "system", "content": mt.system_prompt},
                            {"role": "user", "content": mt.sentence_1.format(action= action)},
                        ]
                    elif i == 3:
                        messages = [
                            {"role": "system", "content": mt.system_prompt},
                            {"role": "user", "content": mt.sentence_1.format(action= action)},
                            {"role": "assistant", "content": mt.response_1},
                            {"role": "user", "content": mt.sentence_2},
                            {"role": "assistant", "content": mt.response_2},
                            {"role": "user", "content": mt.sentence_3},
                        ]
                    elif i == 4:
                        messages = [
                            {"role": "system", "content": mt.system_prompt},
                            {"role": "user", "content": mt.sentence_1.format(action= action)},
                            {"role": "assistant", "content": mt.response_1},
                            {"role": "user", "content": mt.sentence_2},
                            {"role": "assistant", "content": mt.response_2},
                            {"role": "user", "content": mt.sentence_3},
                            {"role": "assistant", "content": mt.response_3},
                            {"role": "user", "content": mt.sentence_4},
                        ]
                    else:
                        messages = [
                            {"role": "system", "content": mt.system_prompt},
                            {"role": "user", "content": mt.sentence_1.format(action= action)},
                            {"role": "assistant", "content": mt.response_1},
                            {"role": "user", "content": mt.sentence_2},
                            {"role": "assistant", "content": mt.response_2},
                            {"role": "user", "content": mt.sentence_3},
                            {"role": "assistant", "content": mt.response_3},
                            {"role": "user", "content": mt.sentence_4},
                            {"role": "assistant", "content": mt.response_4},
                            {"role": "user", "content": mt.sentence_5},
                        ]

                    temp_dict['action'] = action
                    temp_dict['query'] = messages
                    temp_dict['turn'] = i
                    temp_dict['type'] = type_
                    temp_dict['category'] = key
                    attack_data_list.append(temp_dict)
    attack_data_list_dict['gpt_4o_attack_data.json'] = attack_data_list
    attack_data_list_dict['gpt_4o_mini_attack_data.json'] = attack_data_list
    return attack_data_list_dict

def attack_generation_data_ablation():
    mt_m_h = MultiTurnAttack_ablation_three_turn_M_H()
    ### open-source-model
    ablation_data_list_dict = {}
    for model_id in open_model_id_dict.keys():
        tokenizer = AutoTokenizer.from_pretrained(model_id,token=access_token)
        temp_data = []
        for key in harmful_dict.keys():
            for item in harmful_dict[key]:
                temp_dict = {}
                temp_dict['action'] = item
                temp_dict['category'] = key
                temp_dict['turn'] = 'm_h'
                message = [{'role':'system','content':'You are a helpful AI assistant.'},
                            {'role':'user','content':mt_m_h.sentence_1.format(action=temp_dict['action'])},
                            {'role':'assistant','content':mt_m_h.response_1},
                            {'role':'user','content':mt_m_h.sentence_2},
                            {'role':'assistant','content':mt_m_h.response_2},
                            {'role':'user','content':mt_m_h.sentence_3}]
                temp_dict['query'] = tokenizer.apply_chat_template(message,tokenize=False)
                temp_data.append(temp_dict)  
        print(len(temp_data))
        print(len(list(set([item['action'] for item in temp_data]))))
        ablation_data_list_dict[open_model_id_dict[model_id].format("ablation")] = temp_data

    ### close source model
    temp_data = []
    for key in harmful_dict.keys():
        for item in harmful_dict[key]:
            temp_dict = {}
            temp_dict['action'] = item
            temp_dict['category'] = key
            temp_dict['turn'] = 'm_h'
            message = [{'role':'system','content':'You are a helpful AI assistant.'},
                        {'role':'user','content':mt_m_h.sentence_1.format(action=temp_dict['action'])},
                        {'role':'assistant','content':mt_m_h.response_1},
                        {'role':'user','content':mt_m_h.sentence_2},
                        {'role':'assistant','content':mt_m_h.response_2},
                        {'role':'user','content':mt_m_h.sentence_3}]
            temp_dict['query'] = message
            temp_data.append(temp_dict)  
    print(len(temp_data))
    print(len(list(set([item['action'] for item in temp_data]))))
    ablation_data_list_dict['gpt_4o_ablation_data.json'] = temp_data
    ablation_data_list_dict['gpt_4o_mini_ablation_data.json'] = temp_data

    return ablation_data_list_dict



def check_generation_data(attack_data_list_dict):
    ### check data
    for model_key in attack_data_list_dict.keys():
        print("checking data for ", model_key)
        test_data_list = attack_data_list_dict[model_key]
        turns_dict = {}
        for item in test_data_list:
            if item['turn'] not in turns_dict:
                turns_dict[item['turn']] = []
            turns_dict[item['turn']].append(item)

        for key in turns_dict.keys():
            assert len(turns_dict[key]) == 14000

        occupation_dict = {}
        for item in test_data_list:
            if item['type'] not in occupation_dict:
                occupation_dict[item['type']] = []
            occupation_dict[item['type']].append(item)

        for key in occupation_dict.keys():
            assert len(occupation_dict[key]) == 5600

        category_dict = {}
        for item in test_data_list:
            if item['category'] not in category_dict:
                category_dict[item['category']] = []
            category_dict[item['category']].append(item)

        for key in category_dict.keys():
            assert len(category_dict[key]) == 4000

        action_dict = list(set([item['action'] for item in test_data_list]))
        assert len(action_dict) == 1400

        for type in occupation_dict.keys():
            for key in category_dict.keys():
                temp_list = []
                for item in occupation_dict[type]:
                    if item['category'] == key and item['type'] == type:
                        temp_list.append(item['action'])
                    
                assert len(temp_list) == 400
                assert len(list(set([item for item in temp_list]))) == 100

        print("data check passed for ", model_key)

def save_attack_data(attack_data_list_dict,args):
    for model_key in attack_data_list_dict.keys():
        attack_data_list = attack_data_list_dict[model_key]
        write_json_file(attack_data_list, f'./{args.output_path}/{model_key}')



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process Data.')
    parser.add_argument('--action_data_path', type=str, default='./data/beavertail_action_sample.npy', help='data_path')
    parser.add_argument('--output_path', type=str, default='./red_queen_attack', help='output_path')
    parser.add_argument('--type', type=str, default='normal', help='data_type')

    # argstring = ["--action_data_path", './data/beavertail_action_sample.npy', ### data to be evaluated 
    #              "--output_path", './red_queen_attack', ### output path
    #              "--type", 'normal' ### type of data: 1) normal 2) ablation
    #             ]
    # args = parser.parse_args(argstring)
    args = parser.parse_args()
    print('Start Generation')
    harmful_dict = np.load(args.action_data_path, allow_pickle=True).item()
    if args.type == 'normal':
        attack_data_list_dict = attack_generation_data_open()
        attack_data_list_dict = attack_generation_data_closed(attack_data_list_dict)

        print('Start Checking')
        check_generation_data(attack_data_list_dict)
        print('End of Checking')
    else:
        attack_data_list_dict = attack_generation_data_ablation()
    print('End of Generation')

    print('Start Saving')
    save_attack_data(attack_data_list_dict,args)
    print('End of Saving')

