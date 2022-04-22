object l6z3 {
  import scala.io._
  import scala.math._

  def mapWordsCounters(filePath: String): Map[String, Int] = {

    val fileSource = Source.fromFile(filePath)
    val words=fileSource.mkString.toLowerCase.split("\\W+")
    fileSource.close

    words.groupBy(identity).mapValues(_.size)
  }

  def calculateMoment(wordsCounters: Map[String, Int], moment: Int): BigInt = {
    var s: BigInt = 0
    for ((_,m) <- wordsCounters){
      s = s + pow(m, moment).toInt
    }
    s
  }

  def minMaxMoments(n0: Int, n1: Int, real: BigInt) = {

    val momentDivision = n1.toFloat/n0

    val minimal = (pow(momentDivision,2) * n0).toInt
    val single_occurances = (n0 - 1) * pow(1, 2)
    val max_occurance = 1 * pow(n1-n0,2)
    val maximal = (single_occurances + max_occurance).toInt

    print(s"Minimal moment is: $minimal\n")
    print(s"Real moment is: $real\n")
    print(s"Maximal moment is: $maximal\n")

  }


  def main(args:Array[String]):Unit = {

    //TASK3

    val filePath = "canterbury/alice29.txt"
    //val filePath2 = "canterbury/test.txt"

    val map = mapWordsCounters(filePath)

    //val map2 = mapWordsCounters(filePath2)
    //print(map)
    println(calculateMoment(map,0))
    println(calculateMoment(map,1))
    println(calculateMoment(map,2))
    println(calculateMoment(map,3))

    //println(calculateMoment(map2,0))
    //println(calculateMoment(map2,1))
    //println(calculateMoment(map2,2))
    //println(calculateMoment(map2,3))

    //TASK4

    // 0th moment is number of distinct elements in file
    // 1th moment is length of the file


    //TASK5
    minMaxMoments(calculateMoment(map,0).toInt,calculateMoment(map,1).toInt,calculateMoment(map,2).toInt)

  }

}
