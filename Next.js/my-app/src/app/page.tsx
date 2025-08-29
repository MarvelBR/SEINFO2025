import { Button } from "@/components/ui/button";
import { InputPassword } from "@/components/ui/input";
import Link from "next/link";

export default function Home() {
  return (
    <main>
      <div className="bg-red-500">
        Tela Inicial
        <Button asChild>
          <Link href={"/auth/sign-up"}>Tela de Cadastro</Link>
        </Button>
      </div>
      <InputPassword></InputPassword>
    </main>
  );
}
