import streamlit as st


def load_css():
    with open("style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    st.markdown(
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" '
        'integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
        unsafe_allow_html=True)


def st_button(icon, url, label, iconsize):
    if icon == 'github':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-github" viewBox="0 0 16 16" style="color: #0366d6;">
                    <path d="M8 .21a8 8 0 0 0-2.53 15.57c.4.07.55-.17.55-.38v-1.32c-2.25.49-2.72-1.08-2.72-1.08-.37-.95-.9-1.21-.9-1.21-.73-.5.05-.49.05-.49.8.06 1.22.82 1.22.82.71 1.19 1.86.85 2.32.65.07-.53.28-.86.5-1.06-1.75-.2-3.59-.87-3.59-3.88 0-.86.31-1.57.82-2.12-.08-.2-.36-1.01.08-2.1 0 0 .66-.21 2.17.81a7.6 7.6 0 0 1 2-.27c.67 0 1.34.09 2 .27 1.51-1.02 2.17-.81 2.17-.81.44 1.09.16 1.9.08 2.1.51.55.82 1.26.82 2.12 0 3.02-1.85 3.67-3.6 3.87.28.24.53.72.53 1.46v2.17c0 .21.14.46.55.38A8 8 0 0 0 8 .21z"/>
                </svg>
                {label}
            </a>
        </p>
    '''
    
    elif icon == 'leetcode':
        button_code = f'''
        <p>
            <a href="https://leetcode.com/" class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <img src="https://leetcode.com/_next/static/images/logo-dark-c96c407d175e36c81e236fcfdd682a0b.png" width={iconsize} height={iconsize} alt="LeetCode Logo" style="filter: invert(0.7);">
                {label}
            </a>
        </p>
    '''
    
    elif icon == 'linkedin':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                </svg>
                {label}
            </a>
        </p>'''
    
    elif icon == 'hackerrank':
        button_code = f'''
            <p>
                <a href="https://www.hackerrank.com/" class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                    <img src="https://hrcdn.net/fcore/assets/work/header/hackerrank_logo-21e2867566.svg" width={iconsize} height={iconsize} alt="HackerRank Logo" style="filter: invert(0.7);">
                    {label}
                </a>
            </p>
        '''
    
    elif icon == 'codechef':
        button_code = f'''
            <p>
                <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                    <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-code-square" viewBox="0 0 16 16" style="color: #5B4638;">
                        <path d="M2.026 1.032L0 0v13.928h5.6v-1.654h-4.4V1.032zm2.726 0v9.242H8.8V1.032H4.752zM10.4 0H8.374v13.928l2.026 1.032V0zm4.574 1.032l-2.026 1.032v11.864l2.026-1.032V1.032z"/>
                    </svg>
                    {label}
                </a>
            </p>
        '''
    
    
    elif icon == 'codeforces':
        button_code = f'''
            <p>
                <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                    <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-code-square" viewBox="0 0 16 16" style="color: #1F8ACB;">
                        <path d="M3.648 3.636l-.212.082c-.093.036-.214.07-.39.105A.617.617 0 0 0 2 4.45V5H1.5v1h.5v3H1.5v1h.5v1.549c0 .145.01.264.03.358.019.094.082.22.189.376l.176.246L4.064 12h1.28l.65-.007a3.377 3.377 0 0 0 .578-.094c.18-.057.343-.13.488-.22l.17-.106L7.5 10.5h1v1h.5v-1h.5v-1h-.5v-3h.5v-1h-.5V4.45a.617.617 0 0 0-.047-.204c-.027-.07-.094-.193-.201-.37l-.176-.246L8.936 3h-1.28l-.65.007a3.377 3.377 0 0 0-.578.094 1.412 1.412 0 0 0-.488.22l-.17.106zm.578.62l.117-.07c.04-.019.092-.043.158-.07a.72.72 0 0 1 .38 0c.066.027.12.051.157.07l.117.07L5.5 4.764l-.117-.07a.72.72 0 0 1-.158-.07.72.72 0 0 1-.157.07l-.117.07L3.5 4.764l.117-.07a.72.72 0 0 1 .158-.07.72.72 0 0 1 .157.07l.117.07zM3.5 6.128l.117-.07c.04-.019.092-.043.158-.07a.72.72 0 0 1 .38 0c.066.027.12.051.157.07l.117.07L5.5 6.892l-.117-.07a.72.72 0 0 1-.158-.07.72.72 0 0 1-.157.07l-.117.07L3.5 6.892l.117-.07a.72.72 0 0 1 .158-.07.72.72 0 0 1 .157.07l.117.07zM9.5 6.128l.117-.07c.04-.019.092-.043.158-.07a.72.72 0 0 1 .38 0c.066.027.12.051.157.07l.117.07L11.5 6.892l-.117-.07a.72.72 0 0 1-.158-.07.72.72 0 0 1-.157.07l-.117.07L9.5 6.892l.117-.07a.72.72 0 0 1 .158-.07.72.72 0 0 1 .157.07l.117.07zM12.362 3.636l.212.082c.093.036.214.07.39.105A.617.617 0 0 0 14 4.45V5h.5v1h-.5v3h.5v1h-.5v1.549c0 .145-.01.264-.03.358-.019.094-.082.22-.189.376l-.176.246L11.936 12h-1.28l-.65-.007a3.377 3.377 0 0 1-.578-.094c-.18-.057-.343-.13-.488-.22l-.17-.106L8.5 10.5h-1v1h-.5v-1h-.5v-1h.5v-3h-.5v-1h.5V4.45a.617.617 0 0 1 .047-.204c.027-.07.094-.193.201-.37l.176-.246L7.064 3h1.28l.65.007a3.377 3.377 0 0 1 .578.094c.18.057.343.13.488.22l.17.106z"/>
                    </svg>
                    {label}
                </a>
            </p>
        '''
    
    
    elif icon == 'contact':
        button_code = f'''
            <p>
                <a href="mailto:{url}" class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                    <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-envelope" viewBox="0 0 16 16" style="color: #1F8ACB;">
                        <path d="M1.5 3A1.5 1.5 0 0 1 3 1.5h10A1.5 1.5 0 0 1 14.5 3v10a1.5 1.5 0 0 1-1.5 1.5h-10A1.5 1.5 0 0 1 1 13.5v-10zm.293-.293a.5.5 0 0 0-.293.457V13.5A2.5 2.5 0 0 0 3.5 16h10a2.5 2.5 0 0 0 2.5-2.5v-10a.5.5 0 0 0-.854-.353L12 7.793l-5.147-5.146a.5.5 0 0 0-.353-.147zm12 0a.5.5 0 0 0-.353.146L9.5 7.793l-5.147-5.146a.5.5 0 0 0-.706 0L.207 2.207a.5.5 0 0 0 0 .707L6.5 9.293l-.646.647a.5.5 0 0 0 0 .706l5.147 5.147a.5.5 0 0 0 .706 0l5.147-5.147a.5.5 0 0 0 0-.706L14.5 9.293l6.293-6.293a.5.5 0 0 0 0-.707L15.707 2.207z"/>
                    </svg>
                    {label}
                </a>
            </p>
        '''
    
    return st.markdown(button_code, unsafe_allow_html=True)
