#
# PySNMP MIB module APAGENTCAP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APAGENTCAP2-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:38:18 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
acmepacketAgentCapability, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketAgentCapability")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibIdentifier, TimeTicks, ModuleIdentity, mib_2, Bits, ObjectIdentity, iso, Counter32, Gauge32, enterprises, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Integer32, snmpModules = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "ModuleIdentity", "mib-2", "Bits", "ObjectIdentity", "iso", "Counter32", "Gauge32", "enterprises", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Integer32", "snmpModules")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
apAgentCap2Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 2, 2))
apAgentCap2Module.setRevisions(('2020-10-26 00:00', '2021-07-06 00:00', '2022-02-16 00:00', '2022-03-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: apAgentCap2Module.setRevisionsDescriptions(('Added apStirCap', 'Added apStirCap2', 'Added new capability objects apSipMSRPKPIStatsCap for MSRP statistics.', 'Added apNSEPRealmKPIStatsCap and apSmgmtNSEPOutboundSession.',))
if mibBuilder.loadTexts: apAgentCap2Module.setLastUpdated('202203240000Z')
if mibBuilder.loadTexts: apAgentCap2Module.setOrganization('Oracle Communications')
if mibBuilder.loadTexts: apAgentCap2Module.setContactInfo('           \tCustomer Service\n\t\t \tPostal:\t\tOracle Communications\n\t\t\t\t\t100 Crosby Drive \n\t\t\t\t\tBedford, MA 01730\n\t\t\t\t\tUS\n\t\t    \tTel:\t\t1-800-633-0738\n\t\t\tUrl:\t\twww.oracle.com\n\t\t \tE-mail:\t\tsupport@oracle.com')
if mibBuilder.loadTexts: apAgentCap2Module.setDescription(' Agent capability2 MIB for Oracle Communications Acme Packet SBCs.')
apIPForwardMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 1))
apIpForwardCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpForwardCap = apIpForwardCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpForwardCap = apIpForwardCap.setStatus('current')
if mibBuilder.loadTexts: apIpForwardCap.setDescription('Acme Packet Agent Capability IP-FORWARD support.')
apAppsStirMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 2))
apStirCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apStirCap = apStirCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apStirCap = apStirCap.setStatus('current')
if mibBuilder.loadTexts: apStirCap.setDescription('Acme Packet Agent Capability Stir MIB support.')
apStirCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apStirCap2 = apStirCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apStirCap2 = apStirCap2.setStatus('current')
if mibBuilder.loadTexts: apStirCap2.setDescription('Acme Packet Agent Capability Stir Agent MIB support.')
apMSRPKPIMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 3))
apMSRPKPIStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apMSRPKPIStatsCap = apMSRPKPIStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apMSRPKPIStatsCap = apMSRPKPIStatsCap.setStatus('current')
if mibBuilder.loadTexts: apMSRPKPIStatsCap.setDescription('Acme Packet Agent Capability for MSRP KPI statistics  MIB.')
apNSEPRealmKPIMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 4))
apNSEPRealmKPIStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNSEPRealmKPIStatsCap = apNSEPRealmKPIStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNSEPRealmKPIStatsCap = apNSEPRealmKPIStatsCap.setStatus('current')
if mibBuilder.loadTexts: apNSEPRealmKPIStatsCap.setDescription('Acme Packet Agent Capability for NSEP Realm\n                                KPI statistics MIB.')
apNSEPOutboundSessionMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 5))
apSmgmtNSEPOutboundSession = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNSEPOutboundSession = apSmgmtNSEPOutboundSession.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNSEPOutboundSession = apSmgmtNSEPOutboundSession.setStatus('current')
if mibBuilder.loadTexts: apSmgmtNSEPOutboundSession.setDescription('Acme Packet Agent Capability for NSEP\n                                Outbound KPI statistics MIB.')
mibBuilder.exportSymbols("APAGENTCAP2-MIB", apNSEPRealmKPIStatsCap=apNSEPRealmKPIStatsCap, apNSEPOutboundSessionMibCapabilities=apNSEPOutboundSessionMibCapabilities, apAgentCap2Module=apAgentCap2Module, PYSNMP_MODULE_ID=apAgentCap2Module, apStirCap2=apStirCap2, apAppsStirMibCapabilities=apAppsStirMibCapabilities, apNSEPRealmKPIMibCapabilities=apNSEPRealmKPIMibCapabilities, apStirCap=apStirCap, apMSRPKPIMibCapabilities=apMSRPKPIMibCapabilities, apSmgmtNSEPOutboundSession=apSmgmtNSEPOutboundSession, apMSRPKPIStatsCap=apMSRPKPIStatsCap, apIPForwardMibCapabilities=apIPForwardMibCapabilities, apIpForwardCap=apIpForwardCap)
