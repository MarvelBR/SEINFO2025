import { TSignUpInputSchema } from "./sign-up.entity";

export interface IAuthGateway {
  signUp: (param: TSignUpInputSchema) => Promise<void>;
}

