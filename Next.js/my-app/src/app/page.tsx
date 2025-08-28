import { Button } from "@/components/ui/button";
import Link from "next/link";

export default function Home() {
  return (
    <main>
      <div className="bg-red-500">
        Tela Inicial
        <Button asChild>
          <Link href={"/auth/sign-up"}>Voltar a tela inicial</Link>
        </Button>
      </div>
    </main>
  );
}
