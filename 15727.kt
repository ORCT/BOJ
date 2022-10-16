import java.util.*

fun main() = with (Scanner(System.`in`)) {
    var n : Int = nextInt()
    var m : Int = when (n%5) {
        0 -> 0
        else -> 1
    }
    
    println(n/5 + m)
}