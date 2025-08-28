import { Button } from "@/components/ui/button";
import {
  Card,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import Link from "next/link";

const SignUpPage = () => {
  return (
    <section className="flex h-screen w-screen items-center justify-center bg-amber-300 px-5">
      <Card className="w-full max-w-md">
        <CardHeader>
          <CardTitle>Crie sua conta</CardTitle>
          <CardDescription>
            Insira suas informações para realizar o cadastro
          </CardDescription>
        </CardHeader>
      </Card>
      <Button asChild>
        <Link href={"/"}>Voltar a tela inicial</Link>
      </Button>
    </section>
  );
};

//ANOTAR OQ É CADA COISA DO TAILWIND

export default SignUpPage;
