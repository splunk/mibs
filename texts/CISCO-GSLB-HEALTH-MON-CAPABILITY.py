#
# PySNMP MIB module CISCO-GSLB-HEALTH-MON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GSLB-HEALTH-MON-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGslbHealthMonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 536))
ciscoGslbHealthMonCapability.setRevisions(('2007-02-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGslbHealthMonCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGslbHealthMonCapability.setLastUpdated('200702230000Z')
if mibBuilder.loadTexts: ciscoGslbHealthMonCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGslbHealthMonCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal:  170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel:  +1 800 553-NETS\n\n            E-mail:  cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoGslbHealthMonCapability.setDescription('The capabilities description\n        of CISCO-GSLB-HEALTH-MON-MIB.')
ciscoGslbHealthMonCapabilityV02R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 536, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbHealthMonCapabilityV02R00 = ciscoGslbHealthMonCapabilityV02R00.setProductRelease('GSS 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbHealthMonCapabilityV02R00 = ciscoGslbHealthMonCapabilityV02R00.setStatus('current')
if mibBuilder.loadTexts: ciscoGslbHealthMonCapabilityV02R00.setDescription('GSS 2.0 Cisco GSLB HEALTH MON MIB capabilities')
mibBuilder.exportSymbols("CISCO-GSLB-HEALTH-MON-CAPABILITY", PYSNMP_MODULE_ID=ciscoGslbHealthMonCapability, ciscoGslbHealthMonCapabilityV02R00=ciscoGslbHealthMonCapabilityV02R00, ciscoGslbHealthMonCapability=ciscoGslbHealthMonCapability)
