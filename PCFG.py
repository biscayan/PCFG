import re
import glob

#read all files
all_files=glob.glob("corpus/*.prd") #search .prd extension files from the folder

raw_file_char=''

for i in range(len(all_files)):
    with open(all_files[i],'r') as file:
        raw_file=file.read()
        raw_file_char+=raw_file

#data cleansing
raw_data=raw_file_char.split() 
data_char=' '.join(raw_data) #make character from the list

data_paren1=re.sub('\(','( ',data_char) #add space
data_paren2=re.sub('\)',' )',data_paren1)
data=re.sub('[^\w\s\-\*\)\(]','',data_paren2) #delete unnecessary elements

with open('data.prd','w') as data_file:
    data_file.write(data)


#make stack class     
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def empty_check(self):
        if len(self.stack) == 0:
            return True

      
#extract rules from the data
def extract_rule():
        
    input_file=open('data.prd','r')
    output_file=open('data_rule.txt','w')
        
    token_stack=Stack() #use stack class

    for file_data in input_file :  
        tokens=file_data.split() 

        for token in tokens:
                
            if token != ')': #store tokens to the stack until right parenthesis does not come 
                token_stack.push(token)
        
            else :      
                rule_stack=Stack()
                    
                while token_stack.stack[len(token_stack.stack)-1]!='(' : 
                        
                    popped_token=token_stack.pop() #pop tokens from the stack
                    rule_stack.push(popped_token)
                        
                token_stack.pop() # match the number of left and right parentheses 
                left_grammar=rule_stack.pop() #extreact left grammar from the rule 
                   
                output_file.write(left_grammar) #write left grammar to the output file 
                output_file.write('->')
                token_stack.push(left_grammar)  

                while rule_stack.empty_check()!=True: 
                    right_grammar=rule_stack.pop() 
                        
                    output_file.write(right_grammar) #write right grammar to the output file
                    output_file.write(' ') 
                        
                output_file.write('\n') 

    input_file.close()
    output_file.close()
        
extract_rule()


#calculate frequency and probability
def freq_prob():
    
    with open('data_rule.txt','r') as rule_file:
        raw_rules=rule_file.readlines()

    rules=sorted(raw_rules) #alphabetic order sort
    
    rule_dict={} #store all rules
    left_grammar_dict={} #store only left grammars

    for rule in rules:
        rule=rule.strip()
        
        if rule in rule_dict: #if rule is in dictionary, increase value 1
            rule_dict[rule]+=1
        else:
            rule_dict[rule]=1 #if rule is not in dictionary, value is 1

        left_grammar=rule.split('->')[0] # '->' is delimiter, so left grammar is extracted

        if left_grammar in left_grammar_dict: 
            left_grammar_dict[left_grammar]+=1
        else:
            left_grammar_dict[left_grammar]=1 

    #output frequency file        
    with open('data_freq.txt','w') as freq_file:
        for rule_key in rule_dict:
            frequency=rule_dict[rule_key]
            freq_file.write("{0} [frequency: {1}]\n".format(rule_key,frequency))

    #output probability file            
    with open('data_prob.txt','w') as prob_file:
        for rule_key in rule_dict:
            left_grammar_key=rule_key.split('->')[0]
            probability=rule_dict[rule_key]/left_grammar_dict[left_grammar_key]*100 
            prob_file.write("{0} [probability: {1}]\n".format(rule_key,round(probability,10))) 

if __name__ == '__main__':
    freq_prob()

