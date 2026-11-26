#
# PySNMP MIB module CISCO-CONFIG-MAN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CONFIG-MAN-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cconfigManCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 469))
cconfigManCapability.setRevisions(('2005-12-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cconfigManCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cconfigManCapability.setLastUpdated('200512290000Z')
if mibBuilder.loadTexts: cconfigManCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cconfigManCapability.setContactInfo('       Cisco Systems\n\t\t\tCustomer Service\n\t\tPostal: 170 West Tasman Drive\n\t\t\tSan Jose, CA  95134\n\t\t\tUSA\n        \n\t\t\tTel: +1 800 553-NETS\n        \n\t\tE-mail: cs-snmp@cisco.com\n\t\t\tcs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: cconfigManCapability.setDescription('Agent capabilities for \n                 CISCO-CONFIG-MAN-MIB')
cconfigManCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 469, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cconfigManCapabilityIOSXRV2R0CRS1 = cconfigManCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cconfigManCapabilityIOSXRV2R0CRS1 = cconfigManCapabilityIOSXRV2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: cconfigManCapabilityIOSXRV2R0CRS1.setDescription('CISCO-CONFIG-MAN-MIB capabilities\n\t\t\t for IOS XR release 2.0')
mibBuilder.exportSymbols("CISCO-CONFIG-MAN-CAPABILITY", cconfigManCapability=cconfigManCapability, PYSNMP_MODULE_ID=cconfigManCapability, cconfigManCapabilityIOSXRV2R0CRS1=cconfigManCapabilityIOSXRV2R0CRS1)
