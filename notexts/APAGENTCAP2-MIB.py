#
# PySNMP MIB module APAGENTCAP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APAGENTCAP2-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:38:51 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
acmepacketAgentCapability, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketAgentCapability")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, ObjectIdentity, NotificationType, Counter64, IpAddress, Bits, enterprises, mib_2, Gauge32, snmpModules, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "ObjectIdentity", "NotificationType", "Counter64", "IpAddress", "Bits", "enterprises", "mib-2", "Gauge32", "snmpModules", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "TimeTicks", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
apAgentCap2Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 2, 2))
apAgentCap2Module.setRevisions(('2020-10-26 00:00', '2021-07-06 00:00', '2022-02-16 00:00', '2022-03-24 00:00',))
if mibBuilder.loadTexts: apAgentCap2Module.setLastUpdated('202203240000Z')
if mibBuilder.loadTexts: apAgentCap2Module.setOrganization('Oracle Communications')
apIPForwardMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 1))
apIpForwardCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpForwardCap = apIpForwardCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpForwardCap = apIpForwardCap.setStatus('current')
apAppsStirMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 2))
apStirCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apStirCap = apStirCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apStirCap = apStirCap.setStatus('current')
apStirCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apStirCap2 = apStirCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apStirCap2 = apStirCap2.setStatus('current')
apMSRPKPIMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 3))
apMSRPKPIStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apMSRPKPIStatsCap = apMSRPKPIStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apMSRPKPIStatsCap = apMSRPKPIStatsCap.setStatus('current')
apNSEPRealmKPIMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 4))
apNSEPRealmKPIStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNSEPRealmKPIStatsCap = apNSEPRealmKPIStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNSEPRealmKPIStatsCap = apNSEPRealmKPIStatsCap.setStatus('current')
apNSEPOutboundSessionMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 5))
apSmgmtNSEPOutboundSession = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNSEPOutboundSession = apSmgmtNSEPOutboundSession.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNSEPOutboundSession = apSmgmtNSEPOutboundSession.setStatus('current')
mibBuilder.exportSymbols("APAGENTCAP2-MIB", apMSRPKPIStatsCap=apMSRPKPIStatsCap, apSmgmtNSEPOutboundSession=apSmgmtNSEPOutboundSession, apAgentCap2Module=apAgentCap2Module, apAppsStirMibCapabilities=apAppsStirMibCapabilities, apNSEPOutboundSessionMibCapabilities=apNSEPOutboundSessionMibCapabilities, apIPForwardMibCapabilities=apIPForwardMibCapabilities, apIpForwardCap=apIpForwardCap, apNSEPRealmKPIStatsCap=apNSEPRealmKPIStatsCap, apStirCap2=apStirCap2, apNSEPRealmKPIMibCapabilities=apNSEPRealmKPIMibCapabilities, apStirCap=apStirCap, apMSRPKPIMibCapabilities=apMSRPKPIMibCapabilities, PYSNMP_MODULE_ID=apAgentCap2Module)
