
using System;

class SistemiINotave
{
    static void Main(string[] args)
    {
        Console.WriteLine("Mirësevini në Sistemin e Notave!");

        do
        {

            Console.Write("Shkruani pikët për detyrat: ");
            int detyrat = Convert.ToInt32(Console.ReadLine());

            Console.Write("Shkruani pikët për kuizet: ");
            int kuizet = Convert.ToInt32(Console.ReadLine());

            Console.Write("Shkruani pikët për provimin: ");
            int provimi = Convert.ToInt32(Console.ReadLine());


            int praguKalimit = 60;


            int notaMesatare = (detyrat + kuizet + provimi) / 3;

            Console.WriteLine("\nLlogaritja...");
            Console.WriteLine($"Nota mesatare: {notaMesatare}");


            char nota;
            if (notaMesatare >= 90)
            {
                nota = 'A';
            }
            else if (notaMesatare >= 80)
            {
                nota = 'B';
            }
            else if (notaMesatare >= 70)
            {
                nota = 'C';
            }
            else if (notaMesatare >= 60)
            {
                nota = 'D';
            }
            else
            {
                nota = 'F';
            }

            Console.WriteLine($"Nota: {nota}");


            if (notaMesatare >= praguKalimit)
            {
                Console.WriteLine("Urime! Ju keni kaluar kursin.");
            }
            else
            {
                Console.WriteLine("Fatkeqësisht, ju nuk e kaluat kursin.");
            }


            Console.Write("\nDëshironi të llogarisni notën për një student tjetër? (po/jo): ");
        } while (Console.ReadLine().ToLower() == "po");

        Console.WriteLine("Faleminderit për përdorimin e programit!");
    }
}


