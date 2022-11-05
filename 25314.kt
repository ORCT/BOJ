import java.util.*

fun main(){
    val sc = Scanner(System.`in`)
    var n = sc.nextInt()
    if(n%4 == 0){
        n = n/4
    }
    else{
        n = n/4+1
    }
    var result = ""
    for(i in 1..n){
        val l = "long "
        result = result + l
    }
    println("${result}int")
}