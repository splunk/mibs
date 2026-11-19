#
# PySNMP MIB module CISCO-MEDIA-GATEWAY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MEDIA-GATEWAY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMediaGatewayCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 375))
ciscoMediaGatewayCapability.setRevisions(('2004-02-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMediaGatewayCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMediaGatewayCapability.setLastUpdated('200402050000Z')
if mibBuilder.loadTexts: ciscoMediaGatewayCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMediaGatewayCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoMediaGatewayCapability.setDescription('The agent capabilities for CISCO-MEDIA-GATEWAY-MIB.')
cMediaGatewayCapV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 375, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMediaGatewayCapV5R00 = cMediaGatewayCapV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMediaGatewayCapV5R00 = cMediaGatewayCapV5R00.setStatus('current')
if mibBuilder.loadTexts: cMediaGatewayCapV5R00.setDescription('Agent capabilities for VXSM in Release 5.0.0.')
mibBuilder.exportSymbols("CISCO-MEDIA-GATEWAY-CAPABILITY", cMediaGatewayCapV5R00=cMediaGatewayCapV5R00, PYSNMP_MODULE_ID=ciscoMediaGatewayCapability, ciscoMediaGatewayCapability=ciscoMediaGatewayCapability)
