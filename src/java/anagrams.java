static boolean isAnagram(String a, String b) {

     Map<Character, Integer> aDict = new HashMap<>();
     Map<Character, Integer> bDict = new HashMap<>();
     aDict = createDict(a);
     bDict = createDict(b);

     return checkDict(aDict, bDict);
 }

 static Map<Character, Integer> createDict( String s){
     Map<Character, Integer> myDict = new HashMap<>();
     for ( char c : s.toCharArray() ){
         if ( myDict.containsKey(c) ) {
             int t_val = myDict.get(c);
             t_val = t_val + 1 ;
             myDict.put( c, t_val);
         } else {
             myDict.put( Character.toLowerCase(c) , 1 );
         }
     }
     return myDict;
 }

 static boolean checkDict( Map<Character, Integer> aDict, Map<Character, Integer> bDict) {

     int aSize = aDict.size();
     int bSize = bDict.size();

     if ( aSize != bSize ) {

         return false;
     }

     for ( char key : aDict.keySet() ) {

         int aVal = aDict.get(key);
         if ( bDict.containsKey(key) ) {

             int bVal = bDict.get(key);
             if ( bVal != aVal ) {
                 return false;
             }
         } else {
             return false;
         }
     }
     return true;
 }
