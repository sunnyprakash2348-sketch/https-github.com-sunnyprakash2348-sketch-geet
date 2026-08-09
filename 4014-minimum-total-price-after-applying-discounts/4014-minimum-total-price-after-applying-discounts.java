class Solution {
    public static double maxprice(int x,int y){
        double z=(x*(100-y))/100.0;
        return z;
        
    }
    public double minPrice(int[] prices, int[] discounts) {
        double maxpri=0;
        Integer[] price = Arrays.stream(prices).boxed().toArray(Integer[]::new);
        Integer[] discount = Arrays.stream(discounts).boxed().toArray(Integer[]::new);
        Arrays.sort(price,Collections.reverseOrder());
        Arrays.sort(discount,Collections.reverseOrder());
        for(int i=0; i<price.length; i++){
            if(i<discount.length){
                maxpri+=maxprice(price[i],discount[i]);
            }
            else{
                maxpri+=maxprice(price[i],0);
            }
        }
        System.out.println(maxpri);
        return maxpri;
    }
}