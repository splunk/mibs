#
# PySNMP MIB module CISCO-ROUTE-POLICIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ROUTE-POLICIES-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRoutePoliciesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 578))
ciscoRoutePoliciesMIB.setRevisions(('2006-08-18 00:00',))
if mibBuilder.loadTexts: ciscoRoutePoliciesMIB.setLastUpdated('200608180000Z')
if mibBuilder.loadTexts: ciscoRoutePoliciesMIB.setOrganization('Cisco Systems, Inc. ')
ciscoRoutePoliciesMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 578, 0))
ciscoRoutePoliciesMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 578, 1))
ciscoRoutePoliciesMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 578, 2))
crpPolicies = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 578, 1, 1))
if mibBuilder.loadTexts: crpPolicies.setStatus('current')
crpPolicyIfIndex = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 578, 1, 1, 1))
if mibBuilder.loadTexts: crpPolicyIfIndex.setStatus('current')
mibBuilder.exportSymbols("CISCO-ROUTE-POLICIES-MIB", crpPolicyIfIndex=crpPolicyIfIndex, ciscoRoutePoliciesMIBObjects=ciscoRoutePoliciesMIBObjects, ciscoRoutePoliciesMIBConform=ciscoRoutePoliciesMIBConform, PYSNMP_MODULE_ID=ciscoRoutePoliciesMIB, ciscoRoutePoliciesMIB=ciscoRoutePoliciesMIB, ciscoRoutePoliciesMIBNotifs=ciscoRoutePoliciesMIBNotifs, crpPolicies=crpPolicies)
