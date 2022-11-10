import java.util.*

fun main(args:Array<String>) {
    val sc = Scanner(System.`in`)
    val n = sc.nextInt()
    for (i in 1..n) {
        val s = sc.next()
        if (s.length >= 6 && s.length <= 9) {
            println("yes")
        } else {
            println("no")
        }
    }
}