FROM ubuntu:latest

RUN apt-get update

# -- ssh internal start
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:passwordpassword' | chpasswd
RUN sed -i 's/#*PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config


#RUN mkdir -p /root/.ssh/
#COPY authorized_keys/*.pub /root/.ssh/authorized_keys
#RUN chmod -R 600 /root/.ssh


# SSH login fix. Otherwise user is kicked off after login
RUN sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# -- ssh internal start

#RUN /usr/sbin/sshd

EXPOSE 22
#CMD ["tail", "-f", "/dev/null"]

ENTRYPOINT /usr/sbin/sshd -D && tail -f dev/null
