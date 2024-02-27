int lengthOfLastWord(char * s){
    /*find '\0'*/
    int n=0;            // length of last word
    char *end=s;        // charater pointer to count the string
    while(*end!='\0'){
        end++;          // go to the end of string
    }

    /*back to the last letter(skip space)*/
    do{
        end--;   
    }
    while((*end)==' ');
               
    while((*end)!=' '){ //check last word and consider
        n++;
        end--;
        if(s>end)break;
    }      
    return n;

}
