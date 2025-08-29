import { z } from "zod";

export const signUpSchema = z
  .object({
    name: z
      .string({
        error: "O nome precisa ser um texto",
      })
      .min(3, { error: "O nome precisa ter no mínimo 3 letras" })
      .nonempty({ error: "O nome é obrigatório" }),
    email: z
      .email({
        error: "O email precisa ser válido",
      })
      .nonempty({ error: "O email é obrigatório" }),
    password: z
      .string({
        error: "A senha precisa ser um texto",
      })
      .min(6, { error: "A senha precisa ter no mínimo 6 caracteres" })
      .nonempty({ error: "A senha é obrigatória" }),
    confirmPassword: z
      .string({
        error: "A senha de confirmação precisa ser um texto",
      })
      .min(6, {
        error: "A senha de confirmação precisa ter no mínimo 6 caracteres",
      })
      .nonempty({ error: "A confirmação da senha é obrigatória" }),
  })
  .refine((data) => data.password === data.confirmPassword, {
    error: "As senhas não coincidem",
    path: ["confirmpassword"],
  })
  .transform((data) => {
    {
      name: data.name;
      email: data.email;
      password: data.password;
    }
  });