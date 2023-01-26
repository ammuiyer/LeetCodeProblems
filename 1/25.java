class Solution {
    public String longestPalindrome(String s) {

        for (int i=s.length(); i>=0; i--){
            for (int j = 0;  j>s.length()-i+1; j++){
                System.out.println(s.substring(j, j+i));
                 if (isPalindrome(s.substring(j, j+i))){
                     return s.substring(j, j+i);
                 } 
        }
        }


                
        return s.substring(0, 1);
    }
    public Boolean isPalindrome(String s){
        for(int i = 0; i<s.length()/2; i++){
            if(s.charAt(i)!=s.charAt(s.length()-i-1)){
                return false;
            }
        }
        return true;

    }
}