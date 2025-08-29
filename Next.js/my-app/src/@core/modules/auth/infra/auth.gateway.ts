import { AxiosInstance } from "axios";
import { IAuthGateway } from "../domain/auth.gateway";
import { TSignUpInputSchema } from "../domain/sign-up.entity";

export class AuthHttpGateway implements IAuthGateway{
    constructor(private readonly http: AxiosInstance){}

    async signUp(param: TSignUpInputSchema):Promise<void>{
        return await this.http.post('/auth/sign-up', param).then(res => res.data);
    }
}