import java.util.*

fun main() {
    val sc = Scanner(System.`in`)
    var n = sc.next()
    val m:Int = 20000303
    var remain = "0"
    var tmp:Int

    for (i in 0..n.length-1) {
        remain += n[i]
        tmp = remain.toInt() % m
        remain = tmp.toString()
    }
    println(remain)
}