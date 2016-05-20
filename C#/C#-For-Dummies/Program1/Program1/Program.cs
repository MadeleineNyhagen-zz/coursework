using System;

namespace Program1
{
    public class Program
    {
        // This is where the program starts.
        static void Main(string[] args)
        {
            // Prompt user to enter a name:
            Console.WriteLine("Enter your name please: ");

            // Now read the name entered:
            string name = Console.ReadLine();

            // Greet the user with the name that was entered:
            Console.WriteLine("Hello, " + name);

            // Wait for user to acknowledge the results
            Console.WriteLine("Press enter to terminate...");
            Console.Read();

            // to insert a code snippet, press ctrl+k and then ctrl+x, use tab to navigate the ensuing menu and enter to select the desired snippet
            // or, if you have the code snippet shortcut, i.e. 'cw', memorized you can type that and then hit tab twice
            // use ctrl+k and ctrl+s together to wrap a highlighted piece of code in a snippet
        }
    }
}
