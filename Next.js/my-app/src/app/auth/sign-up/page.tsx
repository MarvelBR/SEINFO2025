import { Button } from "@/components/ui/button";
import { InputPassword } from "@/components/ui/input";
import {
  Card,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import Link from "next/link";
import SignUpForm from "./components/sign-up-form";

const SignUpPage = () => {
  return (
    <section className="flex h-screen w-screen items-center justify-center bg-blue-500 px-5">
      <Card className="w-full max-w-md">
        <CardHeader>
          <CardTitle>Crie sua conta</CardTitle>
          <CardDescription>
            Insira suas informações para realizar o cadastro
          </CardDescription>
        </CardHeader>
        <SignUpForm />
      </Card>
    </section>
  );
};

export default SignUpPage;
