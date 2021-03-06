# Copyright 2021 Arrikto Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc

from kubernetes.client.configuration import Configuration


__all__ = [
    "TokenCredentialsBase",
]


class TokenCredentialsBase(abc.ABC):

    def refresh_api_key_hook(self, config: Configuration):
        """Refresh the api key.

        This is a helper function for registering token refresh with swagger
        generated clients.

        Args:
            config (kubernetes.client.configuration.Configuration):
                The configuration object that the client uses.

                The Configuration object of the kubernetes client's is the same
                with kfp_server_api.configuration.Configuration.
        """
        config.api_key["authorization"] = self.get_token()

    @abc.abstractmethod
    def get_token(self):
        raise NotImplementedError()
