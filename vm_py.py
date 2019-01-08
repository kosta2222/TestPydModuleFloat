#listKstrK_opcodes=[
        #["NOOP",0]    ,
        #["IADD",0]    ,
        #["ISUB",0]    ,
        #["IMUL",0]    ,
        #["IDIV",0]    ,
        #["IREM",0]    ,
        #["IPOW",0]    ,
        #["ILT",0]     ,   
        #["IEQ",0]     ,   
        #["BR",1]      ,   
        #["BRT",1]     ,   
        #["BRF",1]     ,  
        #["ICONST",1]  ,   
        #["LOAD",1]    , 
        #["GLOAD",1]   ,  
        #["STORE",1]   ,  
        #["GSTORE",1]  ,  
        #["PRINT",1]   ,  
        #["POP",0]     ,  
        #["CALL",2]    ,  
        #["RET",0]     ,  
        #["STORE_RESULT",1],
        #["LOAD_RESULT",0],
        #["HALT",0]        
#] 
#def func_vmPrintStack_SvectorKfloatKI(par_vectorKfloatK_stack, par_I_count) :
    #print("stack=[");
    #for  i in range(0,par_I_count):
        #print(" {0}".format(par_vectorKfloatK_stack[i]));
    
    #print(" ]\n");

            
#def func_vmPrintInstr_SvectorKintKIrV(vectorKintK_opCode, int_ip) :
    #int_opcode =vectorKintK_opCode[int_ip];
    #listKstrYintK_instr = listKstrK_opcodes[int_opcode];
    #int_nargs=listKstrYintK_instr[1]
    #if (int_nargs==0) :

            #print("%d:  %s\n"%( int_ip,listKstrYintK_instr[0] ));

    #elif (int_nargs==1 and int_opcode!=ICONST) :
            #print("%d:  %s %f\n" %(int_ip, listKstrYintK_instr[0],vectorKintK_opCode[int_ip+1]) )
    #elif (int_nargs==1 and int_opcode==ICONST):
        #bytearray_bAr=bytearray([vectorKintK_opCode[int_ip+1],vectorKintK_opCode[int_ip+2],vectorKintK_opCode[int_ip+3],vectorKintK_opCode[int_ip+4]])
        #print("ICONST",unpack('>f',bytearray_bAr)[0])       
        

    #elif (int_nargs==2) :
        #print("%d:  %s %d %d\n"%(int_ip, listKstrYintK_instr[0],vectorKintK_opCode[int_ip+1],vectorKintK_opCode[int_ip+2] ) )

    #elif (int_nargs==3) :
        #print("%d:  %s %d %d %d\n"%(int_ip, listKstrYintK_instr[0],vectorKintK_opCode[int_ip+1],vectorKintK_opCode[int_ip+2],vectorKintK_opCode[int_ip+3] ))

#class Context:
    #classIvokingContext_invokingContext=None
    #metadata=None
    #returnIp=0
    #locals_=[]
    
    #def __init__(self,
        #int_returnip):
        #self.int_returnip=int_returnip
        #self.locals_=[0]*(26)
    #def __str__(self):
        #return "locals:" + str(self.locals_)
        
  
#class Vm:
    #code=[]
    #steck=[]
    #ip=0
    #sp=-1
    #fp=0
    #trace=False
    #globals_=[]
    #metadata=None
    ##ctx=None

    #def __init__(self,code,nglobals,trace=False):
        #self.code=code
        #self.globals_=[0]*nglobals
        #self.steck=[0]*100
        #self.pole_vectorKclassContextK_funcCont=[Context(0)]*40
        #print("vector<Context>:",self.pole_vectorKclassContextK_funcCont[0])
        #self.trace=trace
        #self.pole_float_registrThatRetFunc=0.0
        
    #def exec_(self,startip):
        ##self.ctx=Context(None,0,26)
        #self.ip=startip
        #self.cpu() 

    #def cpu(self):
        #opcode=-1
        #I_callSp=-1

        #while (self.ip<len(self.code) and opcode!=HALT):
            #opcode=self.code[self.ip] #fetch 

            #if self.trace:
                #print("number opcode:",opcode)
                #func_vmPrintInstr_SvectorKintKIrV(self.code,self.ip)
                #func_vmPrintStack_SvectorKfloatKI(self.steck,10)
            #if (opcode==ICONST):#switch
               
                #self.sp+=1
                #bytearray_bAr=bytearray([self.code[self.ip+1],self.code[self.ip+2],self.code[self.ip+3],self.code[self.ip+4]])
                #self.steck[self.sp]=unpack('>f',bytearray_bAr)[0]
                #self.ip+=4
            #elif opcode==GSTORE:
                #v=self.steck[self.sp]
                ##print('v',v)
                #self.sp-=1
                #self.ip+=1
                #addr=self.code[self.ip]
                #self.globals_[addr]=v 

            #elif opcode==GLOAD:
                #self.ip+=1
                #addr=self.code[self.ip]
                #v=self.globals_[addr]
                #self.sp+=1
                #self.steck[self.sp]=v 
            #elif opcode==NOOP:
                #pass
           
            #elif opcode==HALT:
                #return
            #elif opcode==BR:
                #self.ip+=1
                #self.ip=self.code[self.ip]
                #continue
            #elif opcode==BRT:
                #self.ip+=1
                #addr=self.code[self.ip]
                #if self.steck[self.sp]==TRUE:
                    #self.ip=addr
                    #self.sp-=1 
                    #continue  
            #elif opcode==BRF:
                #self.ip+=1
                #addr=self.code[self.ip]
                #if self.steck[self.sp]==FALSE:
                    #self.ip=addr
                    #self.sp-=1 
                    #continue
            #elif opcode==IADD:
                #b=self.steck[self.sp]
                #self.sp-=1
                #a=self.steck[self.sp]
                #self.sp-=1
                #self.sp+=1
                #self.steck[self.sp]=a+b
            #elif opcode==ISUB:
                #b=self.steck[self.sp]
                #self.sp-=1
                #a=self.steck[self.sp]
                #self.sp-=1
                #self.sp+=1
                #self.steck[self.sp]=a-b 
            #elif opcode==IMUL:
                #b=self.steck[self.sp]
                #self.sp-=1
                #a=self.steck[self.sp]
                #self.sp-=1
                #self.sp+=1
                #self.steck[self.sp]=a*b 
            #elif opcode==IDIV:
                #b=self.steck[self.sp]
                #self.sp-=1
                #a=self.steck[self.sp]
                #self.sp-=1
                #self.sp+=1
                #self.steck[self.sp]=a/b  
            ##elif opcode==LES:
                ##b=self.steck[self.sp]
                ##self.sp-=1
                ##a=self.steck[self.sp]
                ##self.sp-=1
                ##if a<b:
                    ##self.sp+=1 
                    ##self.steck[self.sp]=TRUE#True 
                ##else:
                    ##self.sp+=1
                    ##self.steck[self.sp]=FALSE#False 
            #elif opcode==PRINT:   
                #self.ip+=1
                #int_chisloIzLocalnihKakParametr=self.code[self.ip]
                #if int_chisloIzLocalnihKakParametr!=25:
                  #print("print loc:",self.pole_vectorKclassContextK_funcCont[I_callSp].locals_[int_chisloIzLocalnihKakParametr])
                #else:
                  #print("print ret reg:",self.pole_float_registrThatRetFunc)  
                    

            #elif opcode==LOAD:
                #self.ip+=1
                #regnum=self.code[self.ip]
                #print("Load regnum",regnum,type(regnum))
                #self.sp+=1
                #print("Load I_callSp",I_callSp,type(I_callSp))
                #print("self.pole_vectorKclassContextK_funcCont[I_callSp]",self.pole_vectorKclassContextK_funcCont[I_callSp])
                #print("len(self.pole_vectorKclassContextK_funcCont[I_callSp].locals_)",len(self.pole_vectorKclassContextK_funcCont[I_callSp].locals_))
                #self.steck[self.sp]=self.pole_vectorKclassContextK_funcCont[I_callSp].locals_[regnum]
                #print("Load I_callSp",I_callSp,type(I_callSp))
     
            #elif opcode==STORE:
                #self.ip+=1
                #regnum=self.code[self.ip]
                #self.pole_vectorKclassContextK_funcCont[I_callSp].locals_[regnum]=self.steck[self.sp]
                ##print(self.pole_vectorKclassContextK_funcCont[I_callSp].locals_[regnum])
                #self.sp-=1 
            #elif opcode==STORE_RESULT:
                #self.ip+=1
                #regnum=self.code[self.ip]
                #self.pole_float_registrThatRetFunc=self.pole_vectorKclassContextK_funcCont[I_callSp].locals_[regnum]
                #self.sp-=1   
            #elif opcode==LOAD_RESULT:
                ##self.ip+=1
                ##regnum=self.code[self.ip]
                #self.sp+=1
                #self.steck[self.sp]=self.pole_float_registrThatRetFunc                                
            #elif opcode==CALL:

                #self.ip+=1

                #I_findex=self.code[self.ip]

                #self.ip+=1
                #I_nargs=self.code[self.ip]
                #I_callSp+=1
                #classContext_curContext=self.pole_vectorKclassContextK_funcCont[I_callSp]
                #classContext_curContext.returnIp=self.ip+1
                

                #I_firstarg=self.sp-I_nargs+1

                #for i in range(0,I_nargs):
                    #classContext_curContext.locals_[i]=self.steck[I_firstarg+i]
                #self.sp-=I_nargs
                #self.ip=I_findex
                #continue
            #elif opcode==RET:
                #self.ip=self.pole_vectorKclassContextK_funcCont[I_callSp].returnIp
                #I_callSp-=1
                #continue
            ##elif opcode==INC:
                ##v=self.steck[self.sp]
                ##v+=1
                ##self.steck[self.sp]=v
            ##elif opcode==DEC: 
                ##v=self.steck[self.sp]
                ##v-=1
                ##self.steck[self.sp]=v
            ##elif opcode==MOD:
                ##b=self.steck[self.sp]
                ##self.sp-=1
                ##a=self.steck[self.sp]
                ##self.sp-=1
                ##self.sp+=1
                ##self.steck[self.sp]=a%b 
            ##elif opcode==ABI:
                ##v=self.steck[self.sp]
                ##self.steck[self.sp]=abs(v)
            ##elif opcode==NEQ:#a != b ?
                ##b=self.steck[self.sp]
                ##self.sp-=1
                ##a=self.steck[self.sp]
                ##self.sp-=1
                ##if a!=b:
                    ##self.sp+=1 
                    ##self.steck[self.sp]=TRUE#True 
                ##else:
                    ##self.sp+=1
                    ##self.steck[self.sp]=FALSE#False   
            ##elif opcode==LEQ:#a <= b ?
                ##b=self.steck[self.sp]
                ##self.sp-=1
                ##a=self.steck[self.sp]
                ##self.sp-=1
                ##if a<=b:
                    ##self.sp+=1 
                    ##self.steck[self.sp]=TRUE#True 
                ##else:
                    ##self.sp+=1
                    ##self.steck[self.sp]=FALSE#False    
            ##elif opcode==EQU:#a == b ?
                ##b=self.steck[self.sp]
                ##self.sp-=1
                ##a=self.steck[self.sp]
                ##self.sp-=1
                ##if a==b:
                    ##self.sp+=1 
                    ##self.steck[self.sp]=TRUE#True 
                ##else:
                    ##self.sp+=1
                    ##self.steck[self.sp]=FALSE#False  
            ##elif opcode==GEQ:#a == b ?
                ##b=self.steck[self.sp]
                ##self.sp-=1
                ##a=self.steck[self.sp]
                ##self.sp-=1
                ##if a>=b:
                    ##self.sp+=1 
                    ##self.steck[self.sp]=TRUE#True 
                ##else:
                    ##self.sp+=1
                    ##self.steck[self.sp]=FALSE#False         
            #else:
                #raise Exception("invalid opcode:",opcode," at ip=",(self.ip))

            #self.ip+=1