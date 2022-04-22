object l6z1 {

  def main(args:Array[String]):Unit = {

    val range = 2 to 100
    val loop1 = for (i <- range if i%2 !=0; if i%3 !=0; if i%5 !=0) yield(i * i)
    val loop2 = for (i <- range if i%2 !=0; j <- range if j%2==0) yield(i, j)

    val loop1changed = range.withFilter(i => (i%2 !=0 && i%3 !=0 && i%5 !=0)).map(i => i*i)

    val loop2changed  = range.withFilter(i => i%2 !=0).flatMap(i => range.withFilter(j => j%2==0).map(j => (i,j)))

    println("Is loop1 and loop1changed the same?")
    println(loop1 == loop1changed)
    println("Is loop2 and loop2changed the same?")
    println(loop2 == loop2changed)
  }

}
