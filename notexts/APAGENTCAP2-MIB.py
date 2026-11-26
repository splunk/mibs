#
# PySNMP MIB module APAGENTCAP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APAGENTCAP2-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:13:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
acmepacketAgentCapability, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketAgentCapability")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter32, Unsigned32, enterprises, NotificationType, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, snmpModules, Bits, Integer32, Gauge32, MibIdentifier, Counter64, iso, IpAddress, ObjectIdentity, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "enterprises", "NotificationType", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "snmpModules", "Bits", "Integer32", "Gauge32", "MibIdentifier", "Counter64", "iso", "IpAddress", "ObjectIdentity", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("APAGENTCAP2-MIB", apNSEPRealmKPIStatsCap=apNSEPRealmKPIStatsCap, PYSNMP_MODULE_ID=apAgentCap2Module, apStirCap=apStirCap, apNSEPRealmKPIMibCapabilities=apNSEPRealmKPIMibCapabilities, apSmgmtNSEPOutboundSession=apSmgmtNSEPOutboundSession, apNSEPOutboundSessionMibCapabilities=apNSEPOutboundSessionMibCapabilities, apIpForwardCap=apIpForwardCap, apIPForwardMibCapabilities=apIPForwardMibCapabilities, apAgentCap2Module=apAgentCap2Module, apMSRPKPIStatsCap=apMSRPKPIStatsCap, apStirCap2=apStirCap2, apMSRPKPIMibCapabilities=apMSRPKPIMibCapabilities, apAppsStirMibCapabilities=apAppsStirMibCapabilities)
