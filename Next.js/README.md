# NEXT.JS

1. npx create-next-app@latest --empty
2. Would you like to use TypeScript? **Yes**
3. Which linter would you like to use? › **ESLint**
4. Would you like to use Tailwind CSS? **No**
5. Would you like your code inside a `src/` directory? **Yes**
6. Would you like to use App Router? (recommended) **Yes**
7. Would you like to use Turbopack? (recommended) **Yes**
8. Would you like to customize the import alias (`@/*` by default)? **No**
9. cd my-app
10. npm install tailwindcss @tailwindcss/postcss postcss
11. Criar o postcss.config.mjs (Colocar o código depois)
```tsx
const config = {
    plugins: {
        "@tailwindcss/postcss": {},
    },
};

export default config;
```
12. globals.css (dentro da pasta app) e colocar o **@import 'tailwindcss';**
13. Adicionar no layout.tsx (dentro da pasta app) o **import './globals.css'**
14. npx shadcn@latest init
15. npx shadcn@latest add button card input form sonner
16. npm install react-hook-form zod @hookform/resolvers
17. criar um .env.local com **NEXT_PUBLIC_API_URL= _http://172.16.0.119:3333_**
- o http:// ai o ip da maquina : a porta


**Extensões Importante: Tailwind CSS IntelliSense, Prettier e Colorize**

**O Prettier no linux funciona com _ctrl+shift+i_**

**LEMBRANDO QUE PARA RODAR É SÓ METER _npm run dev_**
**E quando clonar instalar o node com o _npm install_**


## Importante

**ESTUDAR**
1. A ***Clean Arquiteture***
- No caso seria a separação das pastas e etc

2. Dar uma revisada nos arquivos .ts e .tsx