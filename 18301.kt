import java.util.*

fun main(){
    val sc = Scanner(System.`in`)
    var a = sc.nextInt()
    var b = sc.nextInt()
    var c = sc.nextInt()
    var ans = (a+1)*(b+1)/(c+1) - 1
    println(ans)
}