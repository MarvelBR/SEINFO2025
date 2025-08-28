import { Button } from "@/components/ui/button"
import Link from "next/link"

const SignUpPage = () => {
    return (
        <div>
            Cadastro
            <Button asChild>
                <Link href={"/"}>Voltar a tela inicial</Link>
            </Button>
        </div>
    );
};

export default SignUpPage