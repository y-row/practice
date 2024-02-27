/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 * 
 * space:7MB(97%)
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
   struct ListNode* tmp1=l1;
   int carry=0;
   int exitcode=0;
   while(1){
       l1->val+=carry+l2->val;
       if(l1->val>=10){
           carry=1;
           l1->val-=10;
       }
       else carry=0;
       if(l1->next&&l2->next==NULL){
           exitcode=1; //1還有2沒有
            break;
       }
       else if(l2->next&&l1->next==NULL){
           exitcode=2; //2還有1沒有
            break;
       }
       else if(!l2->next&&!l1->next){
           break;
       }
       l1=l1->next;
       l2=l2->next;
   };
   switch(exitcode){
       case 0:
        if(carry==1){
            l1->next=l2;
            l1->next->val=1;
            l1->next->next=NULL;
        }
        break;   
       case 1:
        while(carry==1&&l1->next!=NULL){
            l1=l1->next;
            if(l1->val==9){
                l1->val=0;
            }
            else{
                l1->val+=1;
                carry=0;
                }
        }break; 
       case 2:
       l1->next=l2->next;
        while(carry==1&&l1->next!=NULL){
            l1=l1->next;
            if(l1->val==9){
                l1->val=0;
            }
            else{
                l1->val+=1;
                carry=0;
                }
        }break;
    }
    if(carry){//代表是因為next=NULL跳出
            l1->next=calloc(1,sizeof(struct ListNode));
            l1=l1->next;
            l1->next=NULL;
            l1->val=1;
        }
    return tmp1;
}